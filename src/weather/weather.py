from get_weather import GetWeather
from save_weather_data import SaveWeatherData
import pandas as pd

class Weather:
    def __init__(self):
        self.sw = SaveWeatherData()
        self.vilageFcst_data = None
        self.ultraSrtNcst_data = None

        self.TMN = 0
        self.TMX = 0
        self.REH = 0
        self.POP = 0
        self.PTY = 0
        self.WSD = 0
        self.SKY = 0

        # current temp
        self.T1H = 0

        self.base_date = 00000000
        self.base_time = 0000

        self.gw = None
        self.sw = SaveWeatherData()

    def get_data(self):
        if not self.same_date_time():
            self.vilageFcst_data = self.gw.get_VilageFcst()
            self.ultraSrtNcst_data = self.gw.get_UltraSrtNcst()
        else:
            pass
            #self.vilageFcst_data, self.ultraSrtNcst_data = self.get_data_from_file()

    # check if there it's base time and date is same as previous search
    def same_date_time(self):
        # UltraSrtNcst is used because it's term between base time is shorter
        self.gw = GetWeather()
        u_base_date, u_base_time = self.gw.get_base_time_UltraSrtNcst()
        if u_base_date == self.base_date and u_base_time == self.base_time:
            return True
        else:
            self.base_date = u_base_date
            self.base_time = u_base_time
        return False

    # get weather data from file if base_date and base_time matches
    def get_data_from_file(self):
        pass

    def org_data(self, data: pd.DataFrame):
        index = ['DATE', 'TIME', 'TMN', 'TMX', 'REH', 'POP', 'PTY', 'WSD', 'SKY']
        ret = dict.fromkeys(set(index), 0)
        ret['DATE'] = data[0]['fcstDate']
        ret['TIME'] = data[0]['fcstTime']


w = Weather()
w.get_data()