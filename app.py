from flask import Flask, request
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6534122111:AAGyHhbsCKcIu391JBLSiCZfjmq-SbG97Z0'
bot = telegram.Bot(TOKEN)
chat_id = '5575549228'

# route for index page
@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'