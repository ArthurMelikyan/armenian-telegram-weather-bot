
import pyowm

apikey = "c718050391a59ccb7807ec04f907427f"

owm = pyowm.OWM(apikey)  # You MUST provide a valid API key

city = input('what is your city? :')

observation = owm.weather_at_place(city)

w = observation.get_weather()

get_temp =  w.get_temperature('celsius')['temp_max']

if get_temp < 10:
    print('in  ' + city + ' temperature is ' + str(get_temp))
    print('WTF? wear warm clotes')
elif  get_temp > 10 and get_temp < 15:
    print('in  ' + city + ' temperature is ' + str(get_temp))
    print('Norm temperature')
elif get_temp > 15:
    print('in  ' + city + ' temperature is ' + str(get_temp))
    print('warm temperature')