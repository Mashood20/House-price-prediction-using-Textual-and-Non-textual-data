import json
import requests as req

def run(listingId):

    url = "https://api-graphql-lambda.prod.zoopla.co.uk/graphql"

    payload = "{\"query\":\"query MarketStats($listingId: Int!) {\\n    listingDetails(id: $listingId) {\\n        __typename\\n        ... on ListingData {\\n            counts {\\n                numBedrooms\\n            }\\n            marketStats {\\n                areaName\\n                areaNameUri\\n                propertyTypeGroup\\n                askingPrices {\\n                    toRent {\\n                        meanValue\\n                    }\\n                }\\n                historicalEstimates {\\n                    overMonth\\n                    value\\n                    pctChangeSince\\n                    date\\n                    changeSince\\n                }\\n                sales {\\n                    overYear\\n                    mean\\n                    newBuilds\\n                    numSales\\n                }\\n                recentSales {\\n                    date\\n                    price\\n                    propertyId\\n                    streetAddress\\n                    uri\\n                }\\n            }\\n        }\\n\\n        ... on ListingResultError {\\n            errorCode\\n        }\\n    }\\n}\\n\",\"variables\":{\"listingId\":"+f"{listingId}"+"}}"
    headers = {
        'authority': 'api-graphql-lambda.prod.zoopla.co.uk',
        'accept': 'application/json',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www.zoopla.co.uk',
        'referer': 'https://www.zoopla.co.uk/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu'
    }
    # 'cookie': 'zooplapsid=86f92258c3964d45b144f4c90a20793c; ajs_anonymous_id=93e92b4b51634b939834134c1ca691ed; random_traffic_allocation=78; _ga=GA1.1.1572057636.1707160624; cookie_consents={"schemaVersion":4,"content":{"brand":1,"consents":[{"apiVersion":1,"stored":false,"date":"Mon, 05 Feb 2024 19:17:10 GMT","categories":[{"id":1,"consentGiven":true},{"id":3,"consentGiven":true},{"id":4,"consentGiven":true}]}]}}; _gcl_au=1.1.1635743210.1707160630; _fbp=fb.2.1707160630509.1937023392; permutive-id=8d844389-164e-490c-ba78-9d69ebff2a2f; _pin_unauth=dWlkPVpHTTBNakJrT1RRdFlqazFZUzAwWVRJeExUa3dNbU10TXpJMU1ESm1ZalkyWlRObA; _tt_enable_cookie=1; _ttp=SSxd1SJNmqKeu9mkN_TZ2AKaXjl; ndp_session_id=3e1ee6bd-b9c0-4d40-9876-c112342d3d04; _cs_c=0; __cf_bm=WbQJ7zxXhbz4Z92FVbPLoHnjvJNXE9.aILyxQJ189hw-1707168689-1-Ae5kj4WiBEBqQgtY1v8iNpZtAv0u1w8Dxq9a/rd/psxKN/h3Zw+t8cQWmTWOCza+eP+/Wfqu2engoVMMfcYAL/Q=; cf_clearance=P3yQ5vjtoJnp10GJ8wH2kHZ2vmhhO7gJpMzTP7OCTrE-1707168689-1-AZFr/5nXTt+Aq7WJ+hZU7nj+whpLUuVwY+eLC6Nyhzoj7ltxSL49g6TV8lfK4jqj1rpZynVieqciRczXXfOUVwY=; optExp=1; __gads=ID=8631a41a94da3551:T=1707160633:RT=1707168719:S=ALNI_MYuHhtQn5e8TkuTia-jyxkfiwRDDA; __gpi=UID=00000d11ad3539cc:T=1707160633:RT=1707168719:S=ALNI_Ma7HLYDeZXbGu6KXU0T3butT1YBUA; __eoi=ID=f9f51e8497c723a7:T=1707160633:RT=1707168719:S=AA-AfjYb90gsIVCNc43QlDFIS3lv; zid=e2c345049b3747dd80c2a76790b7d0a6; zooplasid=e2c345049b3747dd80c2a76790b7d0a6; _cfuvid=xNAWp6SONGK9S6Q7Iy.O0obq0gyUnc2Ggt2Ukdtu8v8-1707168746312-0-604800000; active_session=anon; _cs_cvars=%7B%221%22%3A%5B%22page%22%2C%22%2Ffor-sale%2Fdetails%2F%22%5D%2C%222%22%3A%5B%22activity%22%2C%22listing_details%22%5D%2C%223%22%3A%5B%22country_code%22%2C%22gb%22%5D%2C%225%22%3A%5B%22signed_in_status%22%2C%22signed%20out%22%5D%2C%226%22%3A%5B%22property_type%22%2C%22terraced%22%5D%2C%228%22%3A%5B%22ab_test%22%2C%22hide-two%7C_home-check_ee-mvt%22%5D%2C%229%22%3A%5B%22product_category%22%2C%22for-sale%2Fresi%2Fagent%2Fpre-owned%2Fgb%22%5D%2C%2211%22%3A%5B%22outcode%22%2C%22NW8%22%5D%7D; _cs_id=fa78bd26-db30-ae28-e301-0d4f8b697656.1707160726.2.1707168745.1707168420.1.1741324726666.1; _cs_s=5.0.0.1707170545145; _uetsid=291424b0c45b11ee9abc3f47ff3f1011; _uetvid=29149630c45b11eebb4019ff7891004f; cto_bundle=oQHpJl9kVG42Um5NaG95dGFGSVJHc2Q0OEElMkJJM0dPJTJCV2hwMDZBbEliZnc0JTJGejR2YTdxdHJHUnhIMGhWZ244ZSUyRnJtYUdHeUFoemZiYnMxeDJvN25vY21aMTFLQmFlQUg0V2JxcjclMkJGYnE4YWVQNHB1N09keGZBRCUyRnNraGZiTXNIM1BLZmhpWDlTYTJNbXM4c0o0cDE3eEFGRnclM0QlM0Q; _ga_HMGEC3FKSZ=GS1.1.1707168415.2.1.1707168800.60.0.0; _cfuvid=vc313JhI_.UtgIc3XvNiqs_tETP.VZ_pWB3rBboESU4-1707140971880-0-604800000',

    r = req.request("POST", url, headers=headers, data=payload)
    if r.status_code == 200:
        try:
            json_data = json.loads(r.text)
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
    else:
        print(f"Request failed with status {r.status_code}")

    mean = None

    try:
        # ["marketStats"]["sales"][0]["mean"]
        mean = json_data["data"]["listingDetails"]["marketStats"]["sales"][0]["mean"]
    except:
        # keep None value for mean if not present
        pass

    return mean
