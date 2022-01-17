from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def home():
    return "Server for live message count project | Owned by @-BlazingWind- . Thanks!"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()