import configparser

from pytz import timezone as tz

parser = configparser.ConfigParser()
parser.read('envfile.ini', encoding='utf-8')
config = parser['DEFAULT']

timezone = tz('Europe/London')

JWT_ACCESS_SECRET = config.get('JWT_ACCESS_SECRET')
JWT_REFRESH_SECRET = config.get('JWT_REFRESH_SECRET')
