import vk_api
import pandas as pd
import time
import json

vk_session = vk_api.VkApi('89263185183', 'mariamanush123')  # логин и пароль
vk_session.auth()
vk = vk_session.get_api()


def main():
    #    x = vk.friends.get(fields='contacts')

    count_in = vk.groups.getMembers(group_id='thisis_media')
    count = count_in['count']
    print(count)
    offset = 0

    i = 0
    step = 1000
    data = []

    for count in range(count_in['count'], 0, -step):
        y = vk.groups.getMembers(group_id='thisis_media', offset=offset,
                                 fields='contacts, city')
        # data += y['items']
        data.extend(y['items'])
        time.sleep(3)

    df = pd.io.json.json_normalize(data)
    df.to_excel(r'thisis_media.xlsx', index=False)

#https://conversiontools.io/conversion/convert_csv_to_excel #encoding

if __name__ == '__main__':
    main()
