import glob
import os as os
import pandas as pd

path = r'../varsh_data_sets/brookline_brighton_public/'
all_files = glob.glob(os.path.join(path, '*.csv'))


# df = pd.read_csv(path + '/PublicRecord_1.csv')
# print(all_files)

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

# print(concatenated_df)

# Select all duplicate rows based on one column
parsed_df = concatenated_df[concatenated_df.Owner1.notnull()]
duplicateRowsDF = parsed_df[parsed_df.duplicated(['Owner1'])]
print(
    "Duplicate Rows based on a single column are:",
    duplicateRowsDF[
        [
            'Address',
            'Building Value',
            'City',
            'Owner1',
            'Owner2',
            'Year Built',
            'Zip'
        ]
    ].sort_values(by='Owner1'),
    sep='\n'
)
