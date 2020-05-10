import json
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import os
import pandas as pd

def get_base_time(hour):
    hour = int(hour)
    if hour < 3:
        tmp_hour = '20'
    elif hour < 6:
        tmp_hour = '23'
    elif hour < 9:
        tmp_hour = '02'
    elif hour < 12:
        tmp_hour = '05'
    elif hour < 15:
        tmp_hour = '08'
    elif hour < 18:
        tmp_hour = '11'
    elif hour < 21:
        tmp_hour = '14'
    elif hour < 24:
        tmp_hour = '17'
    return tmp_hour + '00'

def get_weather():
    service_key = os.environ.get('VILAGE_FCST_SERVICE_KEY')
    cur_time = datetime.now()
    cur_date = cur_time.strftime('%Y%m%d')
    cur_hour = int(cur_time.strftime('%H'))

    # Need to calculate base time; current time date might not exists
    if cur_hour < 6:
        base_date = str(int(cur_date) - 1)
    else:
        base_date = cur_date
    base_time = get_base_time(cur_hour)
    
    nx = str(62)
    ny = str(122)

    api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst'
    params = '?' + urlencode({
        quote_plus("serviceKey"): service_key,
        quote_plus('numOfRows'): "100",
        quote_plus('pageNo'): "1",
        quote_plus('dataType'): 'JSON',
        quote_plus('base_date'): base_date,
        quote_plus('base_time'): base_time,
        quote_plus('nx'): nx,
        quote_plus('ny'): ny
    })

    req = urllib.request.Request(api_url + unquote(params))
    response_body = urlopen(req).read()
    data = json.loads(response_body)
    res = pd.DataFrame(data['response']['body']['items']['item'])
    print(res)

get_weather()