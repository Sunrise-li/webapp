import sys
sys.path.append('../config/db_config')
import db_config as config
from tables import Tables
import logging
LOGGER = logging.getLogger('db')

class InitDataBase:
    def __init__(self,application=None):
        if application == None:
            LOGGER.error('application is null')
            sys.exit(0)
        application.config.from_object(config)

        self.db = SQLAlchemy(application)
        if self.db == None:
            LOGGER.error('db init error')
            sys.exit(-1)

        from tables_mapper import Tables
        #初始化表对象
        self.tables = Tables(self.db)
        self.create_all()
        LOGGER.info('tables init success...')

    def create_all(self):
        self.db.create_all()
    def insert(self,obj):
        self.db.session.add(obj)
        self.db.session.commit()
    def delete(self,obj):
        self.db.session.delete(obj)
        self.db.session.commit()
    def get(self,obj,id):
        return obj.query.get(id)
    def get_all(self,obj):
        return obj.query.all()

    
