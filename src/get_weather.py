from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import json
import os
import pandas as pd

class GetWeather:
    def __init__(self):
        self.service_key = os.environ.get('VILAGE_FCST_SERVICE_KEY')
        self.current_time = datetime.now()
        self.current_date = self.current_time.strftime('%Y%m%d')
        self.hour = self.current_time.strftime('%H')
        self.minute = self.current_time.strftime('%M')
        self.base_params = '?' + urlencode({
            quote_plus("serviceKey"): os.environ.get('VILAGE_FCST_SERVICE_KEY'),
            quote_plus('numOfRows'): "200",
            quote_plus('pageNo'): "1",
            quote_plus('dataType'): 'JSON',
            quote_plus('nx'): '62',
            quote_plus('ny'): '122'
        })
    
    #초단기실황조회 base_time 계산
    def get_base_time_UltraSrtNcst(self):
        hour = int(self.hour)
        date = int(self.current_date)
        if int(self.minute) < 40:
            hour -= 1
        if hour < 0:
            hour = 23
            date -= 1
        return [str(date), str(hour).zfill(2) + "00"]

    #동네예보조회 base_time 계산
    def get_base_time_VilageFcst(self):
        hour = int(self.hour)
        date = int(self.current_date)
        if int(self.minute) < 10:
            hour -= 1
        if hour < 2:
            hour = 23
            date -= 1
        elif hour < 5:
            hour = 2
        elif hour < 8:
            hour = 5
        elif hour < 11:
            hour = 8
        elif hour < 14:
            hour = 11
        elif hour < 17:
            hour = 14
        elif hour < 20:
            hour = 17
        elif hour < 23:
            hour = 20
        return [str(date), str(hour).zfill(2) + "00"]
    
    def get_FcstFromApi(self, api_url, base_date, base_time):
        extra_param = '&' + urlencode({
            quote_plus('base_date'): base_date,
            quote_plus('base_time'): base_time
        })

        req = urllib.request.Request(api_url + unquote(self.base_params) + unquote(extra_param))
        response_body = urlopen(req).read()
        data = json.loads(response_body)
        res = pd.DataFrame(data['response']['body']['items']['item'])
        return res

    def get_UltraSrtNcst(self):
        api_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
        base_date, base_time = self.get_base_time_UltraSrtNcst()
        try:
            return self.get_FcstFromApi(api_url,base_date,base_time)
        except:
            return None

    def get_VilageFcst(self):
        api_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst"
        base_date, base_time = self.get_base_time_VilageFcst()
        try:
            return self.get_FcstFromApi(api_url,base_date,base_time)
        except:
            return None