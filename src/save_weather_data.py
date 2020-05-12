from csv import DictWriter
from tools import append_dict_as_row
import pandas as pd

class WeatherData:
    def __init__(self):
        # 파일 위치
        self.path = "../data/"
        self.file_name = "weather.csv"
        # 칼럼: 날짜, 최저기온, 최고기온, 습도, 비확률, 비종류, 풍속, 하늘상태
        self.field_names = ['DATE', 'TIME', 'TMN', 'TMX', 'REH', 'POP', 'PTY', 'WSD', 'SKY']

        self.last_base_date = '00000000'
        self.last_base_time = '0000'
        
    # update weather_data
    def set_weather_data(self, data: dict):
        try:
            df = pd.read_csv(self.path + self.file_name)
        except:
            df = pd.DataFrame(columns=self.field_names)
        if df['TIME'] != data['TIME']:
            pass


    # get necessary weather_data
    def get_weather_data(self):
        pass