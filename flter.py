import pandas as pd
FILE_NAME = 'vospitanie_riti_kit16'
# читаем Excel в Pandas DataFrame
df = pd.read_excel(FILE_NAME+r'.xlsx', dtype={'mobile_phone':'str'})

# удаляем все "не цифры"
df['mob_clean'] = df.mobile_phone.str.replace(r'\D','')

# маска фильтра: выбираем номера, в которых минимум 10 цифр
# и которые начинаются на `7` или `8`
mask = (df['mob_clean'].str.len() >= 10) & (df['mob_clean'].str.contains(r'^[78]'))

# заменяем "неправильные" номера на пустую строку
df.loc[~mask, ['mob_clean']] = ''

# сохраняем DataFrame в Excel файл
df.to_excel(FILE_NAME + '' + r'result.xlsx', index=False)