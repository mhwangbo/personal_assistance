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
        self.current_date = current_time.strftime('%Y%m%d')
        self.hour = current_time.strftime('%H')
        self.minute = current_time.strftime('%M')
        self.base_params = '?' + urlencode({
            quote_plus("serviceKey"): os.environ.get('VILAGE_FCST_SERVICE_KEY'),
            quote_plus('numOfRows'): "100",
            quote_plus('pageNo'): "1",
            quote_plus('dataType'): 'JSON',
            quote_plus('nx') = '62',
            quote_plus('ny') = '122'
        })
    #초단기실황조회 base_time 계산
    def get_base_time_UltraSrtNcst(self):
        hour = int(self.hour)
        date = int(self.current_date)
        if self.minute < 40:
            hour -= 1
        if hour < 0:
            hour = 23
            date -= 1
        return [str(date), str(hour).zfill(2) + "00"]

    #동네예보조회 base_time 계산
    def get_base_time_VilageFcst(self):
        hour = int(self.hour)
        date = int(self.current_date)
        if self.minute < 10:
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
    
    def get_UltraSrtNcst(self):
        api_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
        base_date, base_time = self.get_base_time_UltraSrtNcst()
        extra_param = '&' + urlencode({
            quote_plus('base_date'): 
        })