__author__ = 'kaceymiriholston'

from flask import Flask

app = Flask(__name__) #this is the flask instance
app.config.from_object("config")

from GUI_app import views