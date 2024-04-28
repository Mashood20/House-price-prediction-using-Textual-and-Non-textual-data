import json
import requests as req

def run(listingId):

    url = "https://api-graphql-lambda.prod.zoopla.co.uk/graphql"

    payload = "{\"query\":\"query ListingHistory($listingId: Int!) {\\r\\n  listingDetails(id: $listingId) {\\r\\n    __typename\\r\\n    ... on ListingData {\\r\\n      priceHistory {\\r\\n        __typename\\r\\n        ...History\\r\\n      }\\r\\n      viewCount {\\r\\n        __typename\\r\\n        ...ViewCount\\r\\n      }\\r\\n    }\\r\\n    ... on ListingResultError {\\r\\n      __typename\\r\\n      errorCode\\r\\n    }\\r\\n  }\\r\\n}\\r\\n    \\r\\n    fragment History on PriceHistory {\\r\\n  firstPublished {\\r\\n    __typename\\r\\n    firstPublishedDate\\r\\n    priceLabel\\r\\n  }\\r\\n  lastSale {\\r\\n    __typename\\r\\n    date\\r\\n    newBuild\\r\\n    price\\r\\n    priceLabel\\r\\n    recentlySold\\r\\n  }\\r\\n  priceChanges {\\r\\n    __typename\\r\\n    isMinorChange\\r\\n    isPriceDrop\\r\\n    isPriceIncrease\\r\\n    percentageChangeLabel\\r\\n    priceChangeDate\\r\\n    priceChangeLabel\\r\\n    priceLabel\\r\\n  }\\r\\n}\\r\\n    \\r\\n\\r\\n    fragment ViewCount on ViewCount {\\r\\n  viewCount30day\\r\\n}\",\"variables\":{\"listingId\":"+f"{listingId}"+"}}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.zoopla.co.uk/',
        'Content-Type': 'application/json',
        'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu',
        'Origin': 'https://www.zoopla.co.uk',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Cookie': '__cf_bm=WxLclUDUYlQn1_I5HBisBfUchiNVf5NQcE6EMmiM0Zw-1703173402-1-AeYyrw3QkhbXDStYWTsttiPaQbI2U2cJ5qvD3IfgBqKh7U3RW5qnv5onelC+xTiTwQpRNSdO/PM+pdjX/GeKIL8=; _cfuvid=6ws9lnWShGO59ppJQoLiYBX77l6dfLzU82dCW8PIwUw-1703173402730-0-604800000; cf_clearance=PL652SZZiSn3.KzrkXXyebTv6tkcnur3rtxX0LUW54I-1703173403-0-2-25481424.315fb133.72494bc4-250.2.1703173403; zid=b086ddec45754d3f9f1e4a258c64966b; zooplasid=b086ddec45754d3f9f1e4a258c64966b; zooplapsid=defc8ba288f448fca120b4e69b29190e; ajs_anonymous_id=f785f22a5aa34b0b86bc9edc0aa321a6; active_session=anon',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }

    r = req.request("POST", url, headers=headers, data=payload)
    json_data = json.loads(r.text)

    listing_data = []

    try:
        firstPublished = json_data['data']['listingDetails']['priceHistory']['firstPublished']
    except:
        firstPublished = None
    
    try:
        lastSale = json_data['data']['listingDetails']['priceHistory']['lastSale']
    except:
        lastSale = None
    
    if firstPublished is not None:
        firstPublishedDate = str(firstPublished['firstPublishedDate'])[:10]
        firstPublishedPrice = str(firstPublished['priceLabel'])
        listing_data.extend([('first_published_date', firstPublishedDate), ('first_published_price', firstPublishedPrice)])
    
    if lastSale is not None:
        lastSaleDate = str(lastSale['date'])
        lastSalePrice = str(lastSale['priceLabel'])
        listing_data.extend([('last_sale_date', lastSaleDate), ('last_sale_price', lastSalePrice)]) 

    return listing_data