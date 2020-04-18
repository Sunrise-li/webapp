from flask import Flask,request
from hashlib import md5;

app = Flask(__name__)

@app.route('/user/login',methods=['GET','POST'])
def login():
    print(request.args)
    username = request.args.get('username')
    password = request.args.get('password')
    print('username :{0} password {1}'.format(username,password))
    if verify(username,password):
        return 'Success username:{0} password {1} '.format(username,password)
    return 'error'

def verify(username,password):
    if username == None or username == '' or password == None or password == '' :
        return False;
    print(md5(password.encode('utf8')))
    print(md5('123456'.encode('utf8')))
    if username == 'admin' and  md5(password.encode('utf8')) == md5('123456'.encode('utf8')):
        return True;

    return False;

if __name__ == '__main__':
    app.run(debug=True,port=8888)

