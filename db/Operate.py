import sys
sys.path.append('config')
sys.path.append('util')
import db_config as config
from verify import *
from tables import Tables
import logging
from flask_sqlalchemy  import SQLAlchemy
LOGGER = logging.getLogger('db')

class InitDataBase:
    def __init__(self,application=None):
        if application == None:
            sys.exit(0)
        application.config.from_object(config)

        self.db = SQLAlchemy(application)
        if self.db == None:
            sys.exit(-1)

        from tables import Tables
        #初始化表对象
        self.tables = Tables(self.db)
        self.create_all()

    def create_all(self):
        self.db.create_all()

    def insert(self,obj):
        if is_not_null(obj):
            self.db.session.add(obj)
            self.db.session.commit()
    
    def delete(self,obj):
        if is_not_null(obj):
            self.db.session.delete(obj)
            self.db.session.commit()

    def execute(self,sql):
        self.db.session.execute()
    
    def get(self,obj,id):
        return obj.query.get(id)

    def get_all(self,obj):
        return obj.query.all()

    
