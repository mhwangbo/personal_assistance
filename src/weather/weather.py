from get_weather import GetWeather
from save_weather_data import SaveWeatherData

class Weather:
    def __init__(self):
        self.sw = SaveWeatherData()
        self.vilageFcst_data = None
        self.ultraSrtNcst_data = None

        self.DATE = 00000000
        self.TIME = 0000
        self.TMN = 0
        self.TMX = 0
        self.REH = 0
        self.POP = 0
        self.PTY = 0
        self.WSD = 0
        self.SKY = 0

        # current temp
        self.T1H = 0

    def get_data(self):
        gw = GetWeather()
        
        self.vilageFcst_data = gw.get_VilageFcst()
        self.ultraSrtNcst_data = gw.get_UltraSrtNcst()

    def org_data(self):
        pass

w = Weather()
w.get_data()