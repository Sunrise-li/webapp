import config
import json
import sys
from flask import Flask
sys.path.append('util')
sys.path.append('db')

from operate import InitDataBase

from snow_flake import SnowFlake 

class Application:
    def __init__(self,host='127.0.0.1',port='8888',debug=True):
        self.snow_flake = SnowFlake()
        self.app = Flask(__name__)
        self.json = json
        self.host = host
        self.port = port
        self.debug = debug
        self.db = InitDataBase(application=self.app)

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



    









