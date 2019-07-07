import glob
import os as os
import pandas as pd

path = r'../varsh_data_sets/brookline_brighton_public/'
all_files = glob.glob(os.path.join(path, '*.csv'))


# df = pd.read_csv(path + '/PublicRecord_1.csv')
# print(all_files)

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

print(concatenated_df)