from csv import DictWriter
from tools import append_dict_as_row
import pandas as pd

class SaveWeatherData:
    def __init__(self):
        # 파일 위치
        self.path = "../data/"
        self.file_name = "weather.csv"
        # 칼럼: 날짜, 시간, 최저기온, 최고기온, 습도, 비확률, 비종류, 풍속, 하늘상태
        self.field_names = ['DATE', 'TIME', 'TMN', 'TMX', 'REH', 'POP', 'PTY', 'WSD', 'SKY']
        
    # update weather_data
    def set_weather_data(self, data: dict):
        try:
            df = pd.read_csv(self.path + self.file_name)
        except:
            df = pd.DataFrame(columns=self.field_names)
        
        if not df.empty:
            df = self.check_weather_data(df, data)
        else:
            value = [list(data.values())]
            df2 = pd.DataFrame(value, columns=self.field_names)
            df = pd.concat([df, df2])

        df.to_csv(self.path + self.file_name, index=False)


    def check_weather_data(self, df: pd.DataFrame, data: dict):
        last_date = df.tail(1)

        if last_date['DATE'].values[0] == data['DATE']:
            if last_date['TIME'].values[0] == data['TIME']:
                return df

            value = [list(data.values())]
            if data['TMN'] == None:
                value[0][2] = last_date['TMN'].values[0]
            if data['TMX'] == None:
                value[0][3] = last_date['TMX'].values[0]
            print(value)
            df.loc[df['DATE'] == data['DATE']] = value
        else:
            value = [list(data.values())]
            df2 = pd.DataFrame(value, columns=self.field_names)
            df = pd.concat([df, df2])
        return df