import pyowm
owm = pyowm.OWM('')
place=input("В каком городе погода?")
#weather
mgr=owm.weather_manager()
observation=mgr.weather_at_place(place)
w=observation.weather
#temperature
weather=mgr.weather_at_place(place).weather
temp_dict_celsius=weather.temperature('celsius')
#wind
wind_dict_in_meters_per_sec=observation.weather.wind()
wind_dict_in_meters_per_sec['speed']
#sunrise
sunrise_iso=weather.sunrise_time(timeformat='iso')
#rain
rain_dict=w.rain
#rain_dict['1h']
#all units
#print weather&temperature&wind&sunrise all units!!!
print(place+" сейчас "+str(temp_dict_celsius)+" wind "+str(wind_dict_in_meters_per_sec)+" sunrise "+str(sunrise_iso)+" rain " +str(rain_dict))

