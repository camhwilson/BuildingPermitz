from numpy.core.fromnumeric import take

import pandas as pd
from pandas.core.frame import DataFrame

from shifting_functions import determine_colshift, determine_rowshift
from misc_functions import substring_in_list, rename_cols
from df_tolist_functions import df_tolist13, df_tolist2, df_tolist4


filepath1x = 'Market Database\\8-2018.xlsx'

filepath2x = 'Market Database\\9-2016.xlsx'

filepath3 = 'Sample Dataset\\type2.xlsx'

filepath4 = 'Market Database\\9-2020.xlsx'




def extract(filepath):
    datatype = 0
    temp_df = pd.read_excel(filepath, header=None)
    condition = False
    i = 0
    
    #standard column list
    new_list = ['Issue Date', 'Permit No.', 'Ward', 'Parcel', 'Address', 'Owner','Contractor', 'Work Description', 'Cost']

    while True:
        
        search_list = temp_df.iloc[:100,i].tolist()
        if substring_in_list('Permits Issued By Day', search_list):
            return process_dtype2(temp_df, new_list)
        if substring_in_list('PERMITNUMBER', search_list):
            datatype = 4
            break

        if substring_in_list('Issue ', search_list):
            process_dtype1(temp_df)

        if substring_in_list('Permit ', search_list):
            shifted_search_list = temp_df.iloc[:20,i+1].tolist()
            if substring_in_list('Ward', shifted_search_list):
                return process_dtype2(temp_df, new_list)

            if substring_in_list('Date', shifted_search_list):
                datatype = 4
                break
        if substring_in_list('Updated', search_list):
            #datatype 3
            return process_dtype3(temp_df, new_list)
        i+=1


    if datatype == 4:
        dshift = determine_rowshift(temp_df, 'PERMIT')
        temp_df.columns = temp_df.iloc[dshift]
        temp_df = temp_df[dshift+1:]

        #renamed columns
        existing_columns = temp_df.columns.tolist()
        existing_columns_d = ['SNP_NEIGHBORHOOD' if x == 'NEIGHBORHOOD' else x for x in existing_columns]
        existing_columns_de = ['Cost' if x == 'TOTAL PROJECT VALUE' else x for x in existing_columns_d]
        existing_columns_del = ['TYPE OF WORK' if x == 'TYPE OF WORK DESCRIPTION' or x == 'TYPEOFWORKDESCRIPTION' else x for x in existing_columns_de]
        existing_columns_delt = ['Parcel' if x=='FORMATTEDPARCELNUMBER' or x== 'FORMATTED PARCEL NUMBER' else x for x in existing_columns_del]
        existing_columns_delta = ['Address' if x == 'ADDRESSABLEOBJEFORMATTEDADDRES' else x for x in existing_columns_delt]

        new_col_list = rename_cols(existing_columns_delta, new_list)

        renaming_dict = dict(zip(existing_columns, new_col_list))
        temp_df = temp_df.rename(columns=renaming_dict )
        
        #reordered columns
        extra_list = [i for i in new_col_list if "Extra Column" in i]
        new_list.extend(extra_list)
        
        temp_df = temp_df.reindex(columns = new_list)

        return df_tolist4(temp_df)


def process_dtype1(temp_df):
    dshift = determine_rowshift(temp_df, 'Date')
    
    temp_df.columns = temp_df.iloc[dshift]
    temp_df = temp_df[dshift+1:]
    #no need to rename columns
    #no need to reorder columns
    return df_tolist13(temp_df)



def process_dtype3(temp_df, new_list):
    dshift = determine_rowshift(temp_df, 'DATE')
    temp_df.columns = temp_df.iloc[dshift]
    temp_df = temp_df[dshift+1:]
    #renamed columns
    existing_columns = temp_df.columns.tolist()
    new_col_list = rename_cols(existing_columns, new_list)
    renaming_dict = dict(zip(existing_columns, new_col_list))
    temp_df = temp_df.rename(columns=renaming_dict)
    #no need to reorder columns
    return df_tolist13(temp_df)

def process_dtype2(temp_df, new_list):
    dshift = determine_rowshift(temp_df, 'Permit ')
    rshift = determine_colshift(temp_df, 'Permit ')
    first_date = temp_df.iloc[dshift-1, rshift]
    temp_df.columns = temp_df.iloc[dshift]
    temp_df = temp_df[dshift+1:]
    
    existing_columns = temp_df.columns.tolist()
    new_col_list = rename_cols(existing_columns, new_list)
    renaming_dict = dict(zip(existing_columns, new_col_list))
    temp_df = temp_df.rename(columns=renaming_dict)

    return df_tolist2(temp_df, first_date, new_list)