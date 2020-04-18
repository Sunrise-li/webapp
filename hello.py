from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/get/<int:id>')
def get(id):
    return 'param id {0}'.format(id)


if __name__ == '__main__':
    app.run(debug=True,port=8888)