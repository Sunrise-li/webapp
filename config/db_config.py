HOST        = '120.53.22.183'
PORT        = '3306'
DATABASE    = 'test'
USERNAME    = 'root'
PASSWORD    = 'li123...'
DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE) 


SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True