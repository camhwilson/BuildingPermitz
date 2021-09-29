
def df_tolist13(dataframe):
    dataframe = dataframe.dropna(subset=['Permit No.'])
    dataframe_list = []
    for index, row in dataframe.iterrows():
        if '-' in row['Permit No.']:
            temp_list = row.tolist()
            temp_list.append('')
            temp_list.append('')
            temp_list.append('')
            dataframe_list.append(temp_list)
    return dataframe_list



def df_tolist2(dataframe, current_date, new_list):
    dataframe['Issue Date'] = ''
    dataframe = dataframe.reindex(columns = new_list)
    dataframe = dataframe.dropna(subset=['Permit No.'])
    dataframe_list = []
    for index, row in dataframe.iterrows():
        if type(row['Permit No.']) is not str:
            current_date = row['Permit No.']
        if type(row['Permit No.']) is str and '-' in row['Permit No.']:
            row['Issue Date'] = current_date
            temp_list = row.tolist()
            temp_list.append('')
            temp_list.append('')
            temp_list.append('')
            if len(temp_list) > 12:
                print(' Is too long')
            dataframe_list.append(temp_list)
    return dataframe_list


def df_tolist4(dataframe):
    dataframe = dataframe.dropna(subset=['Permit No.'])
    dataframe_list = []
    for index, row in dataframe.iterrows():
        if '-' in row['Permit No.']:
            temp_list = row.tolist()
            dataframe_list.append(temp_list)
    return dataframe_list
