import requests
import datetime
import pandas as pd 
import datetime

json_sismos = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+(datetime.datetime.now() + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S')).json()

df_json_sismos = pd.DataFrame.from_dict(json_sismos["features"])

propiedad_sismo = df_json_sismos.properties

propiedad_sismo = propiedad_sismo.to_json()

df_sismos = pd.read_json(propiedad_sismo).transpose()

coordenadas_sismos = df_json_sismos.geometry

coordenadas_sismos_json = coordenadas_sismos.to_json()

df_coordenadas = pd.read_json(coordenadas_sismos_json).transpose()

df_sismos["coordinates"] = coordenadas_sismos

df_sismos['time'] = pd.to_datetime(df_sismos['time'],unit = 'ms')

df_sismos.time = df_sismos.time -datetime.timedelta(hours=6)      

Final = pd.DataFrame(df_sismos, columns = ['coordenates', 'time', 'updated', 'mag'])
Final.to_csv('example.csv')
