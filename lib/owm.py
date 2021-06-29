from pyowm.owm import OWM
import api_key

def get_weather():
    owm = OWM(api_key.OWM_API_KEY)
    mgr = owm.weather_manager()
    weather = mgr.one_call(lat=37.77993, lon=-121.97802, units='imperial')
    for day in weather.forecast_daily:
        print ('min: ', day.temp['min'], ' max: ', day.temp['max'], '\n', day.weather_code, '\n', day.weather_icon_name, '\n', day.weather_icon_url(), '\n\n')

get_weather()
