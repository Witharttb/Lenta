import requests
import json
from pprint import pprint


def get_url_response(url):
    headers = {
        'Referer': 'https://moscow.online.lenta.com/catalog/49/page/3',
        'Content-Type': 'application/json; charset=utf-8',
        'Origin': 'https://moscow.online.lenta.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Set-Cookie': 'Utk_SssTkn=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/; secure; HttpOnly',
        'Cookie': '_tm_lt_sid=1667986434804.989985; _gcl_au=1.1.236507502.1667986437; _ym_uid=1664714432493752456; _ym_d=1667986437; KFP_DID=5030ee75-2c41-5a78-83bd-d7f9a480c37c; _ym_isad=1; _gid=GA1.2.110401032.1667986441; tmr_lvid=cbd4edd934810d3b73121207b9de56c8; tmr_lvidTS=1664714432786; _tt_enable_cookie=1; _ttp=775250cc-e4b8-4531-bcbb-068e1858aa22; Utk_DvcGuid=3d509df4-db6a-9186-2009-8b25a1493047; Utk_SessionToken=FF902FC452B46C7A5CCC152C8B55D9A9; User_Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36; Is_Search_Bot=false; Utk_MrkGrpTkn=3B57EE1D712588E3ADD90E649F5183AB; agree_with_cookie=true; __gtm_campaign_url=https://moscow.online.lenta.com/?utm_source=blogger&utm_medium=banner&utm_campaign=dayoff&shortlink=q2p8i8re&is_retargeting=true&c=%D0%91%D0%B0%D0%BD%D0%BD%D0%B5%D1%80%20%D0%BD%D0%B0%20%D0%BB%D0%B5%D0%BD%D1%82%D0%B5,%20%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%BE%D0%BD%D0%B0%20%D0%BD%D0%B5%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%B0&pid=banner_dayoff; __gtm_referrer=https://online.lenta.com/; _ga=GA1.4.1757743590.1664714433; _gid=GA1.4.110401032.1667986441; flocktory-uuid=88cb6c43-5031-4898-a268-a807166a2fcb-1; adrdel=1; adrcid=ARzog7zc069rTJM2mGJSnYA; afUserId=64972aff-a750-4fe7-81a4-d5cf423a295a-p; AF_SYNC=1667989008006; _a_d3t6sf=duCWqPDjUGxCY_cYHsueVPux; qrator_msid=1667988968.367.fPIPR0Am2KNyokYm-uo1d27tv1lnnujvb5tg38e5kpmhnudgc; _gat_UA-327775-40=1; _gat_UA-327775-1=1; _dc_gtm_UA-327775-40=1; tmr_detect=0|1667996461992; tmr_reqNum=45; _ga_JHCTT9DN5N=GS1.1.1667996452.2.1.1667996477.0.0.0; _ga=GA1.1.1757743590.1664714433'

    }

    payload = {
        "Head": {
            "RequestId": "fd947996c73548e3f5fe1cb65ec88da8",
            "MarketingPartnerKey": "mp80-661295c9cbf9d6b2f6428414504a8deed3020641",
            "Version": "angular_web_0.0.2",
            "Client": "angular_web_0.0.2",
            "Method": "goodsItemSearch",
            "DeviceId": "3d509df4-db6a-9186-2009-8b25a1493047",
            "Domain": "moscow",
            "Store": "utk",
            "SessionToken": "FF902FC452B46C7A5CCC152C8B55D9A9"},
        "Body": {
            "Return": {
                "Barcode": 0,
                "Cart": 0,
                "Description": 0,
                "GoodsCategoryList": 0,
                "GoodsCategoryTree": 1,
                "GoodsDescriptionList": 0,
                "Url": 0,
                "AllCrosslinks": 0,
                "CatalogueFilters": 0,
                "Properties": 0,
                "LandingData": 0,
                "AllProperties": 0,
                "IgnoreStock": 0},
            "Offset": 0,
            "Filters": "",
            "OrderPreset": "category-popular",
            "Count": 0,
            "addictive": 'false',
            "GoodsCategoryId": "49"}}

    r = requests.post(url=url, headers=headers, data=payload)

    return r


if __name__ == '__main__':
    pprint(get_url_response('https://moscow.online.lenta.com/api/rest/goodsItemSearch').json())
