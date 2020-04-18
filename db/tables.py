class Tables:
    def __init__(self,db):
        self.db = db
        self.rigister_tables

        #初始化表对象
        self.rigister_tables = {}

    def rigister_tables(self):
    
    def _new_(self):
        return self
    def get_table(self,table_name):
        if table_name != None and table_name.strip() != '':
            return self.rigister_tables[table_name]
        return None

    def new_admin(self,id=None,name = None,email = None):
        table =self;
        db = self.db
        class Admin(db.Model):
            
            __tablename__ = 'admin'
            __table_args__ = {'extend_existing': True}
            id = db.Column(db.BigInteger,primary_key=True)
            name = db.Column(db.String(80),unique=True)
            email = db.Column(db.String(80),unique=True)
            def __init__(self,id,name,email):
                table.rigister_tables[self.__tablename__] = self
                self.id = id
                self.name = name
                self.email = email
            def keys(self):
                return ('id','name','email')
            def __getitem__(self, item):
                return getattr(self, item)
            def _new_(self):
                return table.rigister_tables.get(self.__tablename__)()


        return Admin(id,name,email)


