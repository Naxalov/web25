from flask import Flask
# Create the application instance
app = Flask(__name__)

# route for index page
@app.route('/')
def index():
    return 'Hello World!!!'