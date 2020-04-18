import config
import json
import sys
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from snow_flake import SnowFlake 

class Application:
    def __init__(self,host='127.0.0.1',port='8888',debug=True):
        self.snow_flake = SnowFlake()
        self.app = Flask(__name__)
        self.app.config.from_object(config)
        self.json = json
        self.host = host
        self.port = port
        self.debug = debug
        self.db = DBOperate(application=self.app)

    def to_json(self,obj):
        if isinstance(obj,(list,dict)):
            ds = []
            for o in obj:
                ds.append(dict(o))
            return json.dumps(ds,ensure_ascii=False)
        else:
            return json.dumps(dict(obj))

    def start(self):
        self.app.run(host=self.host,port=self.port,debug=self.debug)

    def snow_id(self):
        return self.snow_flake.id()

class ObjEncode(json.JSONEncoder):
    pass



class DBOperate:
    def __init__(self,application=None):
        if application == None:
            sys.exit(0)
        self.db = SQLAlchemy(application)
        if self.db is not None:
            from tables_mapper import Tables
            tables = Tables(self.db)
            self.tables = tables
        self.create_all()
    
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

    









