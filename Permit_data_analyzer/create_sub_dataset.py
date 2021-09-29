import pandas as pd
from misc_function import match_pct

drywall_list = ['JC orr', 'JLJI']
curtainwall_list = ['Gurtner', 'River City Glass']
hvac_plumbing_list = ['Renick', 'Ruthrauff Sauer', 'McKamish', 'SSM', 'Tomko', 'Vrabel', 'Wayne Crouse'
                        'Spaeder', 'Jay Reynolds', 'Lugaila', 'Renick', 'Scalise']
electric_list = ['Kirby', 'Ferry', 'Hatzel', 'Marsula', 'Clista', 'Farfield', 'Levit', 'Lighthouse'
                    'Sargent', 'Bronder', 'Pittsburgh Elect', 'Westmoreland']
steel_list = ['Amthor', 'Laswell', 'Sippel', 'Burchick']

sub_dict = {'Drywall': drywall_list, 'Curtainwall': curtainwall_list, 'HVAC/Plumbing': hvac_plumbing_list, 
                        'Electric': electric_list, 'Steel': steel_list}

permitdata = pd.read_csv('dataset.csv')


def create_sub_dataset(subs, dataframe):
    master_li = []
    for index, row in dataframe.iterrows():
        sub_name = str(row['Contractor'])
        for key, value in subs.items():
            for i in value:
                if i.lower() in str(sub_name.lower()):
                    row_list = row.tolist()
                    row_list.append(key)
                    master_li.append(row_list)
    return master_li

master_df = pd.DataFrame(create_sub_dataset(sub_dict, permitdata), columns = ['OldIndex','IssueDate', 'PermitNo.', 'Ward', 'Parcel', 'Address', 'Owner','Contractor', 'WorkDescription', 'Cost', 'SNPNeighborhood(partial)', 'TypeofWork(partial)', 'TypeofStructure(partial)', 'Trade'])
master_df = master_df.drop_duplicates()
master_df.to_csv('Sub_Dataset.csv')