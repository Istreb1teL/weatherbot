import pyowm
import telebot
bot=telebot.TeleBot('1462800551:AAEWI2bHxtIIXQqsEnjlOTZCvLnsYFKLT9s')
owm = pyowm.OWM('b05210473d9ed3a20deeef9644d3f2e9')
#keyboard
keyboard1=telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('temperature', 'wind', 'sunrise')

#bot
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Weather forecast', reply_markup=keyboard1)
    
    mgr=owm.weather_manager()
    observation=mgr.weather_at_place(message.text)
    w=observation.weather
    weather=mgr.weather_at_place(message.text).weather
    temp_dict_celsius=weather.temperature('celsius') #temperature
    wind_dict_in_meters_per_sec=observation.weather.wind() #wind
    wind_dict_in_meters_per_sec['speed']
    sunrise_iso=weather.sunrise_time(timeformat='iso') #sunrise

    if message.text.lower() == 'temperature':
        answer=(message.text+" сейчас "+str(temp_dict_celsius))
        bot.send_message(message.chat.id,answer)
    elif message.text.lower() == 'wind':
        answer=(message.text+" сейчас "+" wind "+str(wind_dict_in_meters_per_sec))
        bot.send_message(message.chat.id,answer)
    elif message.text.lower() == 'sunrise':
        answer=(message.text+" сейчас "+" sunrise "+str(sunrise_iso))
        bot.send_message(message.chat.id,answer)
    #answer=(message.text+" сейчас "+str(temp_dict_celsius)+" wind "+str(wind_dict_in_meters_per_sec)+" sunrise "+str(sunrise_iso))
    #bot.send_message(message.chat.id,answer)
bot.polling(none_stop=True)
#rain
#rain_dict=mgr.weather_at_place(place).observation.rain
#rain_dict['1h']


