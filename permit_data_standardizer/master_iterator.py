import pandas as pd
from individual_file import extract
import os
import time




def preform_iteration(target_folder, new_csvname):

    master_df = pd.DataFrame(columns= ['IssueDate', 'PermitNo.', 'Ward', 'Parcel', 'Address', 'Owner','Contractor', 'WorkDescription', 'Cost', 'SNPNeighborhood(partial)', 'TypeofWork(partial)', 'TypeofStructure(partial)'])

    i = 0
    master_list = []
    for subdir, sep, files in os.walk(target_folder):
        for filename in files:
            i += 1
            filepath = subdir + os.sep + filename
            print('Working on: ' + filename)
            master_list.extend(extract(filepath))   


    master_df = pd.DataFrame(master_list, columns = master_df.columns)
    master_df['Issue Date'] =pd.to_datetime(master_df.IssueDate)
    master_df = master_df.sort_values(by='Issue Date')
    master_df = master_df.reset_index(drop=True)
    master_df.to_csv(new_csvname)

    



start_time = time.time()
preform_iteration('permit_data_standardizer/Market Database','consolidated_dataset.csv')
print()
print('No Errors Detected')
print('Total Run Time: '+str(round((time.time() - start_time), 2))+'s')
