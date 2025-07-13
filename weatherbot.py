import pyowm
import telebot
bot=telebot.TeleBot('1462800551:AAEWI2bHxtIIXQqsEnjlOTZCvLnsYFKLT9s')
owm = pyowm.OWM('b05210473d9ed3a20deeef9644d3f2e9')
#bot
@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr=owm.weather_manager()
    observation=mgr.weather_at_place(message.text)
    w=observation.weather
    weather=mgr.weather_at_place(message.text).weather
    temp_dict_celsius=weather.temperature('celsius')
    wind_dict_in_meters_per_sec=observation.weather.wind()
    wind_dict_in_meters_per_sec['speed']
    sunrise_iso=weather.sunrise_time(timeformat='iso')
    answer=(message.text+" сейчас "+str(temp_dict_celsius)+" wind "+str(wind_dict_in_meters_per_sec)+" sunrise "+str(sunrise_iso))
    bot.send_message(message.chat.id,answer)
bot.polling(none_stop=True)
#rain
#rain_dict=mgr.weather_at_place(place).observation.rain
#rain_dict['1h']


