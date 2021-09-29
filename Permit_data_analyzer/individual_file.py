
import pandas as pd
from misc_function import date_valid

permitdata = pd.read_csv('dataset.csv')


def gc_case_study(searchgc, dataframe):
    search_dict = {}  
    for index, row in dataframe.iterrows():
        gc_name = row['Contractor']
        if searchgc in str(gc_name).lower():
            search_dict[row['IssueDate']]=[row['Parcel'], row['Owner']]
    
    key_list = list(search_dict.keys())
    val_list = list(search_dict.values())
    list_of_all_projects = []
    for index, row in dataframe.iterrows():
        specific_search = [row['Parcel'], row['Owner']]
        date_in_question = row['IssueDate']
        if specific_search in search_dict.values():
            positions =[i for i, x in enumerate(val_list) if x == specific_search]
            for i in positions:
                if date_valid(key_list[i], date_in_question, 1):
                    list_of_all_projects.append(row.tolist())
    return list_of_all_projects

master_df = pd.DataFrame(gc_case_study('mascaro', permitdata), columns = ['OldIndex','IssueDate', 'PermitNo.', 'Ward', 'Parcel', 'Address', 'Owner','Contractor', 'WorkDescription', 'Cost', 'SNPNeighborhood(partial)', 'TypeofWork(partial)', 'TypeofStructure(partial)'])
master_df = master_df.drop_duplicates()
master_df.to_csv('Mascaro.csv')