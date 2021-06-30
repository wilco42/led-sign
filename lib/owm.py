from pyowm.owm import OWM
import api_key

def get_weather():
    owm = OWM(api_key.OWM_API_KEY)
    mgr = owm.weather_manager()
    weather = mgr.one_call(lat=37.77993, lon=-121.97802, units='imperial')
    current = weather.forecast_hourly[0].to_dict()
    current_temp = round(current['temperature']['temp'])
    current_weather_code = current['weather_code']

    for day in weather.forecast_daily:
        # {'reference_time': 1625342400, 'sunset_time': 1625369604, 'sunrise_time': 1625316641, 'clouds': 5, 'rain': {}, 'snow': {}, 'wind': {'speed': 9.17, 'deg': 248, 'gust': 11.95}, 'humidity': 30, 'pressure': {'press': 1013, 'sea_level': None}, 'temperature': {'day': 83.1, 'min': 54.79, 'max': 83.1, 'night': 56.59, 'eve': 65.05, 'morn': 61.23, 'feels_like_day': 81.3, 'feels_like_night': 56.23, 'feels_like_eve': 64.31, 'feels_like_morn': 60.53}, 'status': 'Clear', 'detailed_status': 'clear sky', 'weather_code': 800, 'weather_icon_name': '01d', 'visibility_distance': None, 'dewpoint': 48.43, 'humidex': None, 'heat_index': None, 'utc_offset': None, 'uvi': 10.4, 'precipitation_probability': 0}
        temp = day.to_dict()
        print ('min: ', temp['temperature']['min'], ' max: ', temp['temperature']['max'], '\n', temp['weather_code'], '\n', temp['reference_time']  ,'\n\n')

get_weather()
