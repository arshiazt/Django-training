from decouple import config,Csv
from .base import *

DEBUG = config('DEBUG',default=True,cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())