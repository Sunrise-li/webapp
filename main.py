import sys
sys.path.append('server')
from application import Application

app = Application()
app.start()