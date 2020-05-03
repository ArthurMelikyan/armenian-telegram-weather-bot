import telebot,pyowm

from pyowm.exceptions import api_response_error

bot = telebot.TeleBot("___")
apikey = "___"
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
