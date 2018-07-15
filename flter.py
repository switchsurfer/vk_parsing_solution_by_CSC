import pandas as pd

# читаем Excel в Pandas DataFrame
df = pd.read_excel(r'thisis_media.xlsx', dtype={'mobile_phone':'str'})

# удаляем все "не цифры"
df['mob_clean'] = df.mobile_phone.str.replace(r'\D','')

# маска фильтра: выбираем номера, в которых минимум 10 цифр
# и которые начинаются на `7` или `8`
mask = (df['mob_clean'].str.len() >= 10) & (df['mob_clean'].str.contains(r'^[78]'))

# заменяем "неправильные" номера на пустую строку
df.loc[~mask, ['mob_clean']] = ''

# сохраняем DataFrame в Excel файл
df.to_excel(r'thisis_media_true.xlsx', index=False)