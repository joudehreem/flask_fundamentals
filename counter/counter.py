from flask import Flask, render_template,session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
  if 'key_name' in session:
    session['key_name']=1
    print("key 'key_name' does NOT exist")
  else:
      print('key exists!')
      session['key_name']+=1
  return render_template('index.html',visitor=session['key_name'])

@app.route('/destroy_session')
def clear():
  session.clear()		# clears all keys
  session.pop('key_name',0)# clears a specific key
  return render_template('index.html')
if __name__=="__main__":
  app.run(debug=True)