import pyowm
owm = pyowm.OWM('')
place=input("В каком городе?")
#weather
observation=owm.weather_at_place(place)
w=observation.get_weather()
#temperature
temp=w.get_temperature('celsing')["temp"]
#print weather&temperature
print("В каком городе?"+place+"сейчас"+w.get_detailed_status())
print("Темпаратура сейчас"+str(temp))
if temp <10:
    print ("Сейчас холодно")
elif temp <20:
    print("Сейчас ужасно холодно")
else:
    print("Можно идти на улицу")
