import vk_api
import pandas as pd
import time
import json

vk_session = vk_api.VkApi('your_login', 'your_password')  # login and password
vk_session.auth()
vk = vk_session.get_api()


def main():
    
    count_in = vk.groups.getMembers(group_id='id_your_public')
    count = count_in['count']
    print(count)
    offset = 0

    i = 0
    step = 1000
    data = []

    for count in range(count_in['count'], 0, -step):
        y = vk.groups.getMembers(group_id='id_your_public', offset=offset,
                                 fields='contacts, city')
        data.extend(y['items'])
        time.sleep(3)

    df = pd.io.json.json_normalize(data)
    df.to_excel(r'thisis_media.xlsx', index=False)

if __name__ == '__main__':
    main()
