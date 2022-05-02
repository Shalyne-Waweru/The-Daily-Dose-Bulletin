from flask import Blueprint

#Initialize the Blueprint class
main = Blueprint('main',__name__)

from . import views,error