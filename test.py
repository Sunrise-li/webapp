from application import Application
from tables_mapper import Tables;

#user = Admin('张三','sunrise_di@163.com')
 
app = Application()
app.start()
admin = app.db.tables.new_admin()
#app.db.insert(admin)

# result = app.db.get(admin,'2686546772636991488')
# print(result)
# print(app.to_json(result))



