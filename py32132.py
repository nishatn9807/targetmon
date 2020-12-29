import random
import requests
from threading import Thread


proxy_list = ["http://kqfpdd:gtojpg@139.190.30.91:17102",
"http://xnikty:atogsw@139.190.31.95:17102",
"http://jyyuap:fqqwfz@139.190.30.113:17102",
"http://skbiur:uqbrdt@139.190.31.143:17102",
"http://lxwjmf:dmxzxi@139.190.28.176:17102",
"http://veyauu:flnrlp@139.190.29.231:17102",
"http://pnrjuw:piosct@139.190.31.32:17102",
"http://uaqnyu:oushge@139.190.29.174:17102",
"http://rigrjd:ovsgmp@139.190.31.31:17102",
"http://pkagwk:rnvokb@139.190.29.85:17102",
"http://zkbhmr:sezadg@139.190.31.170:17102",
"http://dadkzo:rssdbk@139.190.29.207:17102",
"http://esyfqz:kkzbtg@139.190.31.45:17102",
"http://itkpla:iifvzl@139.190.31.122:17102",
"http://sjpxls:qlfdnc@139.190.28.161:17102",
"http://nttiwn:ozvrio@139.190.28.179:17102",
"http://qcclal:smvnjg@139.190.28.47:17102",
"http://dvrnbf:puenan@139.190.30.19:17102",
"http://bkxwex:fyatha@139.190.29.169:17102",
"http://jmumuj:mvlvfh@139.190.30.115:17102",
"http://gqsbac:giuqfh@139.190.31.160:17102",
"http://yattzw:ezqfcb@139.190.28.127:17102",
"http://pemaow:dvzcuy@139.190.29.241:17102",
"http://escvif:bdqrfv@139.190.29.252:17102",
"http://xfjlpt:qavjqu@139.190.28.33:17102",
"http://5fd448-accfdcc4d60c:fb432593a191@45.149.220.138:63421",
"http://5fd448-8cf9ed57ec16:609a559141f7@45.149.220.140:63421",
"http://5fd448-58d9771b5b11:21e5d0e32d86@45.149.220.141:63421",
"http://5fd448-eb77404c981a:168e9b8f4836@45.149.220.142:63421",
"http://5fd448-6a7afdca6d6e:57a455c4eedf@45.149.220.143:63421",
"http://5fd448-1e42adb40458:55765709efe5@45.149.220.135:63421",
"http://5fd448-c6d4a9921a8c:df903f5d9fcb@45.149.220.137:63421",
"http://5fd448-0fca6a6f22a7:02354406d67a@45.149.220.136:63421",
"http://5fd448-fa33988fe409:4b62dc167bc8@45.149.220.139:63421",
"http://5fd448-23807d7becdd:1c4c1516c08b@45.149.220.145:63421",
"http://5fd448-5249100a8d8f:738b101d7646@45.149.220.148:63421",
"http://5fd448-0aea12d787a0:e1cfc79585e1@45.149.220.150:63421",
"http://5fd448-dba1c5df869c:520af506fc22@45.149.220.149:63421",
"http://5fd448-f722da0bce1a:7c74a69d2114@45.149.220.147:63421",
"http://5fd448-798e564def08:2b9a91a39ff9@45.149.220.146:63421",
"http://5fd448-401c2b12ef7d:9944a42a7051@45.149.220.144:63421",
"http://5fd448-3524cfd557eb:ad013b9aa14f@45.149.220.152:63421",
"http://5fd448-e0c2a50a009d:4e79741e0811@45.149.220.151:63421",
"http://5fd448-926da414160b:c38583f91cd1@45.149.220.153:63421",
"http://5fd448-92a2642fd1df:46f32c3aa3ac@45.149.220.155:63421",
"http://5fd448-5ec21d1ee9f7:b82716a397b0@45.149.220.156:63421",
"http://5fd448-4ed7562ad866:80ed63bdba12@45.149.220.157:63421",
"http://5fd448-22123df54315:b01e4fddb0d9@45.149.220.158:63421",
"http://5fd448-b7b4a2ca3524:86fb3942741b@45.149.220.159:63421",
"http://5fd448-112b4deb7638:fceeed606826@45.149.220.154:63421",
]
store_locations = ['1401', '3230', '1344', '2212', '1849', '2850', '3243', '2451', '3284', '3276', '3249', '3321', '2840', '3229', '1150', '3312', '3277', '3268', '3334', '3237', '2380', '1886', '2811', '2475', '1263', '1865', '1798', '3291', '3259', '1139', '3236', '1887', '2753', '1822', '1330', '1885', '2381', '1315', '1264', '2006', '3235', '2141', '1192', '1084', '1467', '1866', '1147', '1055', '1358', '1175','1401', '3230', '1344', '2212', '1849', '2850', '3243', '2451', '3284', '3276', '3249', '3321', '2840', '3229', '1150', '3312', '3277', '3268', '3334', '3237', '2380', '1886', '2811', '2475', '1263', '1865', '1798', '3291', '3259', '1139', '3236', '1887', '2753', '1822', '1330', '1885', '2381', '1315', '1264', '2006', '3235', '2141', '1192', '1084', '1467', '1866', '1147', '1055', '1358', '1175']

def monitor(locations):
    headers = {
                'authority': 'redsky.target.com',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'accept': 'application/json',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                'origin': 'https://www.target.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.target.com/p/wahl-lithium-ion-pro-men-s-cordless-haircut-kit-with-finishing-trimmer-soft-storage-case-79600-3301/-/A-13794872',
                'accept-language': 'en-US,en;q=0.9,ar-JO;q=0.8,ar;q=0.7',
                "referrer": "https://www.target.com/p/wahl-lithium-ion-pro-men-s-cordless-haircut-kit-with-finishing-trimmer-soft-storage-case-79600-3301/-/A-13794872",
                 "referrerPolicy": "no-referrer-when-downgrade",
    }
    proxy = random.choice(proxy_list)
    print(proxy)
    while(True):
        for x in locations:
            PID = '81114595'
            proxy = {"http": proxy}
            URL = "https://redsky.target.com/redsky_aggregations/v1/web/pdp_fulfillment_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&tcin={}&store_id={}&store_positions_store_id={}&has_store_positions_store_id=true&pricing_store_id={}".format(PID,x,x,x)
            f = requests.get(URL,proxies=proxy,headers=headers)
            res = f.json()
            ava_status = res['data']['product']['fulfillment']['store_options'][0]['in_store_only']['availability_status']
            if(ava_status !='OUT_OF_STOCK' and ava_status !='NOT_SOLD_IN_STORE'):
                print('{} IN STOCK').format(x)
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/793333840248700942/DKwPk7i_GXK7Ce1YHrmdF54YYGtGkMYc0coUggrBZNHi7eAjykHlm6QkXGAMeYrgVMyY')
                embed = DiscordEmbed(title='{} has restocked'.format(PID), description='https://www.target.com/p/-/A-{}'.format(PID), color=242424)
                webhook.add_embed(embed)
                response = webhook.execute()
            print('{} at {} '.format(ava_status,x))


for i in range(10):
    t = Thread(target=monitor(store_locations))
    print('Started Thread #'+str(i))
    t.start()
