import pyowm
import telebot

from telebot import types
bot=telebot.TeleBot('')
owm = pyowm.OWM('')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print('text message:', message.text)
    place = message.text
    keyboard=types.InlineKeyboardMarkup(True)
    key_temperature=types.InlineKeyboardButton(text='temperature',callback_data='temperature ' + place)
    keyboard.add(key_temperature)
    key_wind=types.InlineKeyboardButton(text='wind',callback_data='wind ' + place)
    keyboard.add(key_wind)
    key_sunrise=types.InlineKeyboardButton(text='sunrise',callback_data='sunrise ' + place)
    keyboard.add(key_sunrise)
    bot.send_message(message.from_user.id,'Weather forecast for ' + place,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    mgr=owm.weather_manager()
    weather = None
    what, place = call.data.split()
    print('text:', call.message.text, 'data:', call.data, 'what:', what, 'place:', place)
    
    try:
        weather=mgr.weather_at_place(place).weather
        temp_dict_celsius=weather.temperature('celsius') #temperature
        wind_dict_in_meters_per_sec=weather.wind() #wind
        sunrise_iso=weather.sunrise_time(timeformat='iso') #sunrise
    except Exception as e:
        bot.send_message(call.message.chat.id, 'Error: ' + repr(e))
        
    try:
        if weather:
            if what == 'temperature':
                answer=(place +" сейчас "+str(temp_dict_celsius))
                bot.send_message(call.message.chat.id,answer)
            elif what == 'wind':
                answer=(place +" сейчас "+" wind "+str(wind_dict_in_meters_per_sec))
                bot.send_message(call.message.chat.id,answer)
            elif what == 'sunrise':
                answer=(place + " сейчас "+" sunrise "+str(sunrise_iso))
                bot.send_message(call.message.chat.id,answer)
    except Exception as e:
        print (repr(e))

bot.polling(none_stop=True)
#rain
#rain_dict=mgr.weather_at_place(place).observation.rain
#rain_dict['1h']


