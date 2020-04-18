class Tables:
    def __init__(self,db):
        
        self.db = db

        self.init_tables()
    
    def init_tables(self):
    
        self.admin()
    
    def admin(self,id=None,name = None,email = None):
    
        db = self.db
    
        class Admin(db.Model):
    
            __tablename__ = 'admin'
    
            __table_args__ = {'extend_existing': True}
    
            id = db.Column(db.BigInteger,primary_key=True)
    
            name = db.Column(db.String(80),unique=True)
    
            email = db.Column(db.String(80),unique=True)
            
            def __init__(self,id,name,email):
    
                self.id = id
    
                self.name = name
    
                self.email = email
            
            def keys(self):
                return ('id','name','email')

            def __getitem__(self, item):
                return getattr(self, item)
        return Admin(id,name,email)


