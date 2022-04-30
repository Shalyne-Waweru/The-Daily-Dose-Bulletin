from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
#The 'instance_relative_config' allows us to connect to the instance/folder when the app instance is created.
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)

#Connects to the instance/config.py file and all its contents are appended to the app.config.
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views