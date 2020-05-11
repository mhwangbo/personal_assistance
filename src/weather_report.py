from get_weather import GetWeather
import pandas as pd

class WeatherReport:
    def extract_UltraSrtNcst(self, data):
        temp_data = data.loc[data['category'] == 'T1H']
        perc_data = data.loc[data['category'] == 'RN1']

        temp = temp_data['obsrValue']
        perc = (str(int(perc_data['obsrValue'])) + "mm 미만") if int(perc_data['obsrValue']) < 100 else ("70mm 이상")

        return {"temp": float(temp), "perc": perc}

    def extract_VilageFcst(self, data):
        min_temp_data = data.loc[data['category'] == 'TMN']
        max_temp_data = data.loc[data['category'] == 'TMX']
        prob_rain_data = data.loc[data['category'] == 'POP']
        rain_type = data.loc[data['category'] == 'PTY']
        sky_data = data.loc[data['category'] == 'SKY']

        print (min_temp_data)
        print (max_temp_data)
        print (prob_rain_data)
        print (rain_type)
        print (sky_data)


weather = GetWeather()
short = weather.get_UltraSrtNcst()
vilage = weather.get_VilageFcst()
report = WeatherReport()
print(report.extract_UltraSrtNcst(short))
print(report.extract_VilageFcst(vilage))