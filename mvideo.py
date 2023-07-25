import requests
import json


cookies = {
    'MVID_TIMEZONE_OFFSET': '5',
    'MVID_CITY_ID': 'CityCZ_2030',
    'MVID_REGION_ID': '5',
    'MVID_REGION_SHOP': 'S953',
}

headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=580d1537f49f447c83379f64d7196a31,sentry-sample_rate=0.5',
    # 'cookie': '__lhash_=276ad958f79664c50142a4925cb87aee; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PODELI_PDP=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SP=true; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; _ym_uid=1661803366903130096; _ym_d=1690144859; _gid=GA1.2.1452133490.1690144859; SMSError=; authError=; advcake_track_id=f91d7b2b-a9f1-a585-ee83-8cbcfb36ddc7; advcake_session_id=69a60348-6310-8de4-896d-0cc3e9e1e8e6; MVID_GEOLOCATION_NEEDED=false; MVID_CITY_CHANGED=true; MVID_CREDIT_DIGITAL=true; MVID_TIMEZONE_OFFSET=5; MVID_CITY_ID=CityCZ_2030; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_CASCADE_CMN=2; MVID_KLADR_ID=6600000100000; __rhash_=77a73bd8e5a6722d375571c98d322435; __hash_=8fa60c8930a6a22d375f045b00972092; _sp_ses.d61c=*; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.1537477108.1690144859; _sp_id.d61c=c957dad4-3ea9-44d6-a518-5aef63c275b2.1690144859.7.1690220886.1690196226.baae006c-3cec-48b4-b849-c8b7662233e6.94dea58a-119d-4aa7-9b80-5fef843871f2.c175a361-367b-46ed-990d-2de3aab58515.1690220440404.56; gssc218=; gsscgib-w-mvideo=c6na6yZJCRXpyMcxIUs7H8c6lwOFpBrA599oqOS7cYpQevFB2eRhidQYlUCFp71dDLLC3LgNB5gDAPjIXe0hXawogSnXVfql7kXisTsY8ssFFgNswlRENipzqL429nyrUT59fJnCY0l2fovTvVCLxUwA/5zcK4WpKD9I/Kfq8+ff4T5YGtkvsTPmwjZMu19hzlUVNZpapk9nxUMyoCRtfLvaxAbt89uMiiX2SJ76djAw9sUTFrtSDlzuE6wF0A==; gsscgib-w-mvideo=c6na6yZJCRXpyMcxIUs7H8c6lwOFpBrA599oqOS7cYpQevFB2eRhidQYlUCFp71dDLLC3LgNB5gDAPjIXe0hXawogSnXVfql7kXisTsY8ssFFgNswlRENipzqL429nyrUT59fJnCY0l2fovTvVCLxUwA/5zcK4WpKD9I/Kfq8+ff4T5YGtkvsTPmwjZMu19hzlUVNZpapk9nxUMyoCRtfLvaxAbt89uMiiX2SJ76djAw9sUTFrtSDlzuE6wF0A==; fgsscgib-w-mvideo=mEOd39caa3b37813cd959b3408a1d66356013022; fgsscgib-w-mvideo=mEOd39caa3b37813cd959b3408a1d66356013022; cfidsgib-w-mvideo=1H7pqWG0pRNApPh17AGIB6SUfpMyyZezHqL3YGOZ93wUnVz+PlPKZ6+9k3ii1IgpJgLdjKXIaJtFA8VpFd1gtxFU4+oZmGQSXNdJ7qujqdS+V5viMDwCVOCss32SQ+X00immY2/1I967y0Y1rWQ6Y/MGyKqbVKdi9MStRcA=; _ga_CFMZTSS5FM=GS1.1.1690220433.7.1.1690220900.0.0.0; _ga_BNX5WPP3YK=GS1.1.1690220433.7.1.1690220900.21.0.0',
    'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65/f/category=4k-uhd-televizory-1682/tolko-v-nalichii=da/diagonal=75---81?sort=price_asc',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '580d1537f49f447c83379f64d7196a31-be4b05a403b9c60b-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    'x-set-application-id': 'f8d92f6c-7759-4f4a-a3e7-d4312268e3b8',
}

listing_params = {
    'categoryId': '65',
    'offset': '0',
    'limit': '24',
    'sort': 'price_asc',
    'filterParams': [
        'WyJjYXRlZ29yeSIsIiIsIjRrLXVoZC10ZWxldml6b3J5LTE2ODIiXQ==',
        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'WyJkaWFnb25hbCIsIiIsIjc1LS0tODEiXQ==',
    ],
    'doTranslit': 'true',
}






def get_data_from_mvideo():
    fin_list = {}
    listing_response = requests.get('https://www.mvideo.ru/bff/products/listing', params=listing_params, cookies=cookies,
                            headers=headers)

    # print(listing_response.json().get('body').get('products'))
    json_data = {
        'productIds': listing_response.json().get('body').get('products'),
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    list_response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data)

    # print(list_response.json())

    for i in list_response.json().get('body').get('products'):
        fin_list.update(
            {str(i['productId']): [i['name']]}
        )

    # print(fin_list)

    id_list_to_str = ",".join(str(i) for i in listing_response.json()['body']['products'])

    prices_params = {
        'productIds': id_list_to_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    prices_response = requests.get('https://www.mvideo.ru/bff/products/prices', params=prices_params,
                                   cookies=cookies, headers=headers)

    # print(prices_response.json())

    for i in prices_response.json().get('body').get('materialPrices'):
        fin_list[i['productId']].append(i['price']['salePrice'])

    # print(fin_list)

    with open('mvideo_data.txt', 'w') as file:
        json.dump(fin_list, file)

get_data_from_mvideo()
