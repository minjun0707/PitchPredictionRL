import pandas as pd

# load dataset
df = pd.read_csv(r'SFBB Player ID Map.csv')

# drop rows with nan values
df = df.dropna()

# only select active players
df = df[df["ACTIVE"] == 'Y']

# only select pitchers
# result_df = df.loc[ (df["ALLPOS"] == 'P') | (df["ALLPOS"] == 'RP') | (df["ALLPOS"] == 'SP') | (df["ALLPOS"] == 'SP/RP') ]
df = df[df["POS"] == 'P']

# select only two needed columns
final_df = df[['MLBID', 'MLBNAME']]
print(final_df.head(10))
final_df.to_csv(r'ID.csv',index = False)



