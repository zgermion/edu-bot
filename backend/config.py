import configparser

config = configparser.ConfigParser()
config.read('CONFIG.INI')

TOKEN = config['TELEGRAM']['token']
TOKEN_DB = config['MONGODB']['token']

DB_logs = config['MONGODB']['logs']
DB_logs_umessage = config['MONGODB']['umessage']

DB_lesson = config['MONGODB']['lesson_db']
COLL_lesson = config['MONGODB']['lesson_coll']

DB_user = config['MONGODB']['user_db']
COLL_user = config['MONGODB']['user_coll']