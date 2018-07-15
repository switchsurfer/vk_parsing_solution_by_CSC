import pandas as pd

# read Excel in Pandas DataFrame
df = pd.read_excel(r'thisis_media.xlsx', dtype={'mobile_phone':'str'})

# delete all except numbers
df['mob_clean'] = df.mobile_phone.str.replace(r'\D','')

# filter mask: select numbers with at least 10 digits 
# and that start with` 7 ' or ' 8`
mask = (df['mob_clean'].str.len() >= 10) & (df['mob_clean'].str.contains(r'^[78]'))

# model the "wrong" number on the blank line
df.loc[~mask, ['mob_clean']] = ''

# save DataFrame to Excel file
df.to_excel(r'thisis_media_true.xlsx', index=False)
