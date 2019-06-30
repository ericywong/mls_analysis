# This script is a template for all other analysis related to timeline graphs
# This is part of the Real Estate data analysis suite.
import numpy as np
import os as os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# We want to create bar graphs of the number of multifamilies sold within a time frame
# based on square footage. Then with each unit sold, we can look at the price + trends
DATA_ROOT_DIR = os.path.dirname('~/Documents/Real Estate/mlsDataSets/mlsSearchBostonDataSets/')
fields = [
    'ANT_SOLD_DATE',
    'SQUARE_FEET',
    'SOLD_PRICE_PER_SQFT'
]
# Full list of curated fields
# fields = [
#     'BEDRMS_1_MF',
#     'BEDRMS_2_MF',
#     'BEDRMS_3_MF',
#     'BEDRMS_4_MF',
#     'BEDRMS_5_MF',
#     'NO_UNITS_MF',
#     'ANT_SOLD_DATE',
#     'ASSESSMENTS',
#     'LIST_PRICE',
#     'LIST_PRICE_PER_SQFT',
#     'LOT_SIZE',
#     'MF_TYPE_MF',
#     'PRICE_PER_SQFT',
#     'SALE_PRICE',
#     'SOLD_PRICE_PER_SQFT',
#     'SQUARE_FEET',
#     'STATE',
#     'STATUS',
#     'TAX_YEAR',
#     'TAXES',
#     'TOWN',
#     'YEAR_BUILT',
#     'ZIP_CODE',
#     'ZIP_CODE_4',
# ]


# print(pd.read_csv(
#     DATA_ROOT_DIR + '/Somerville/somerville_mf_4_2017_4_2019_somerville_mf_24_months_042019.csv',
#     usecols=fields
# ))

df = pd.read_csv(
    DATA_ROOT_DIR + '/Somerville/somerville_mf_4_2017_4_2019_somerville_mf_24_months_042019.csv',
    usecols=fields,
    dtype={'ANT_SOLD_DATE': 'str', 'SQUARE_FEET': 'float', 'SOLD_PRICE_PER_SQFT': 'float'},
    parse_dates=['ANT_SOLD_DATE']
    )

parsed_df = df[df.ANT_SOLD_DATE.notnull()].dropna().sort_values(by='ANT_SOLD_DATE')
# print(parsed_df)

# Create a pie chart of the number of multifamilies with their sqft sold
# in the past two years.
sqft_categories = [
        "0-1000 sqft",
        "1001-1500 sqft",
        "1501-2000 sqft",
        "2001-2300 sqft",
        "2301-2600 sqft",
        "2601-2900 sqft",
        "2901-3100 sqft",
        "3101-3400 sqft",
        "3401+ sqft"
    ]

parsed_df['bins'] = pd.cut(
    parsed_df['SQUARE_FEET'],
    bins=[0, 1001, 1501, 2001, 2301, 2601, 2901, 3101, 3401, 10000],
    labels=sqft_categories
)
parsed_df = parsed_df.groupby(['bins']).size()
# print(parsed_df)

index = 0
sqft_categories_with_mf_number = []
for cat in sqft_categories:
    count = parsed_df[index]
    # print(count)
    if count > 0:
        sqft_categories_with_mf_number.append(cat + '\ncount: ' + str(count))
    index = index + 1

parsed_df_without_zeros = []
for grouped in parsed_df:
    if grouped > 0:
        parsed_df_without_zeros.append(grouped)

plt.pie(parsed_df_without_zeros, labels=sqft_categories_with_mf_number)
plt.title('Somerville MF sold 4-2017 - 4-2019 by sqft')
# plt.show()

# Search for multifamilies with 2301-2600 sqft

bar_df = pd.read_csv(
    DATA_ROOT_DIR + '/Somerville/somerville_mf_4_2017_4_2019_somerville_mf_24_months_042019.csv',
    usecols=fields,
    dtype={'ANT_SOLD_DATE': 'str', 'SQUARE_FEET': 'float', 'SOLD_PRICE_PER_SQFT': 'float'},
    parse_dates=['ANT_SOLD_DATE']
    )

parsed_bar_df = df[df.ANT_SOLD_DATE.notnull()].dropna().sort_values(by='ANT_SOLD_DATE')

# print(parsed_bar_df)
mf_sqft_btw_2301_2600_df = parsed_bar_df.loc[
    (parsed_bar_df['SQUARE_FEET'] >= 2301) &
    (parsed_bar_df['SQUARE_FEET'] <= 2600)]
print(mf_sqft_btw_2301_2600_df)
avg_price_per_sqft_by_date = mf_sqft_btw_2301_2600_df.groupby(['ANT_SOLD_DATE']).mean().drop(['SQUARE_FEET'], axis=1)
print(avg_price_per_sqft_by_date)
avg_price_per_sqft_by_date.plot.line(subplots=False, title='Average Price/Sqft Somerville MF 2301-2600sqft')
plt.show()

# speed = [0.1, 17.5, 40, 48, 52, 69, 88]
# lifespan = [2, 8, 70, 1.5, 25, 12, 28]
# index = [
#          'snail', 'pig', 'elephant',
#          'rabbit', 'giraffe', 'coyote', 'horse'
#         ]
# print(mf_sqft_btw_2301_2600['SOLD_PRICE_PER_SQFT'])
# print(mf_sqft_btw_2301_2600['ANT_SOLD_DATE'])
# df = pd.DataFrame(
#     {'PRICE_PER_SQFT': mf_sqft_btw_2301_2600['SOLD_PRICE_PER_SQFT']},
#     index=mf_sqft_btw_2301_2600['ANT_SOLD_DATE'])
# df.plot.bar(rot=0)
# plt.show()

