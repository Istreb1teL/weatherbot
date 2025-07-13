import pyowm
import telebot
from telebot import types
bot=telebot.TeleBot('1462800551:AAEWI2bHxtIIXQqsEnjlOTZCvLnsYFKLT9s')
owm = pyowm.OWM('b05210473d9ed3a20deeef9644d3f2e9')

#bot
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    keyboard=types.InlineKeyboardMarkup(True)
    key_temperature=types.InlineKeyboardButton(text='temperature',callback_data='temperature')
    keyboard.add(key_temperature)
    key_wind=types.InlineKeyboardButton(text='wind',callback_data='wind')
    keyboard.add(key_wind)
    key_sunrise=types.InlineKeyboardButton(text='sunrise',callback_data='sunrise')
    keyboard.add(key_sunrise)
    bot.send_message(message.from_user.id,'Weather forecast',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    mgr=owm.weather_manager()
    place=call.message.text
    #observation=mgr.weather_at_place(place)
    #w=observation.weather
    weather=mgr.weather_at_place(place).weather
    temp_dict_celsius=weather.temperature('celsius') #temperature
    wind_dict_in_meters_per_sec=observation.weather.wind() #wind
    wind_dict_in_meters_per_sec['speed']
    sunrise_iso=weather.sunrise_time(timeformat='iso') #sunrise

    if call.data == 'temperature':
        answer=(message.text+" сейчас "+str(temp_dict_celsius))
        bot.send_message(call.message.chat.id,answer)
    elif message.text.lower() == 'wind':
        answer=(message.text+" сейчас "+" wind "+str(wind_dict_in_meters_per_sec))
        bot.send_message(call.message.chat.id,answer)
    elif message.text.lower() == 'sunrise':
        answer=(message.text+" сейчас "+" sunrise "+str(sunrise_iso))
        bot.send_message(call.message.chat.id,answer)
    #answer=(message.text+" сейчас "+str(temp_dict_celsius)+" wind "+str(wind_dict_in_meters_per_sec)+" sunrise "+str(sunrise_iso))
    #bot.send_message(message.chat.id,answer)
bot.polling(none_stop=True)
#rain
#rain_dict=mgr.weather_at_place(place).observation.rain
#rain_dict['1h']


