from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#Create the bootstrap instance
bootstrap = Bootstrap()

def create_app(config_name):

  # Initializing application
  #The 'instance_relative_config' allows us to connect to the instance/folder when the app instance is created.
  app = Flask(__name__)

  # Setting up configuration
  app.config.from_object(config_options[config_name])

  # Initializing Flask Extensions
  bootstrap.init_app(app)

  # Registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  # Setting config
  from .request import configure_request
  configure_request(app)

  return app