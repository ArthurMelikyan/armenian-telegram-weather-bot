import telebot,pyowm

from pyowm.exceptions import api_response_error

bot = telebot.TeleBot("855506609:AAE1CIDCHLbnMhB3ROrZWnQ8vHDBRc8sq_Y")
apikey = "c718050391a59ccb7807ec04f907427f"
owm = pyowm.OWM(apikey) 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	# bot.reply_to(message ,message.text)

    try:
        observation = owm.weather_at_place(message.text)

        w = observation.get_weather()

        get_temp =  w.get_temperature('celsius')['temp_max']
        answer = message.text +'-ում ' + str(get_temp) + '° է'
        bot.send_message(message.chat.id, answer)
    except api_response_error.NotFoundError:
        answer = 'Գրեք ճիշտ քաղաքի անուն'
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
