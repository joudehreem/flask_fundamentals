from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello World!"

@app.route('/dojo')
def dojo():
  return 'Dojo!'

@app.route('/say/<name>')
def say(name):
  return 'Hi '+name+'!'

@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):
  return str(num)+' '+word  

@app.errorhandler(404)
def error(e):
  return 'Sorry! No response. Try again.',404 
if __name__=='__main__':
    app.run(debug=True)