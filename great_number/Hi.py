from flask import Flask, render_template,session,request,redirect
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'number'not in session:
        session['number']=random.randint(1,100)
    if 'answer' not in session:
        session['answer']=0
    if 'color' not in session:
        session['color']=0
    if 'attempt' not in session:
        session['attempt']=0

    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def random_number(): 
    guess=int(request.form['random'])  
    session['attempt']+=1
    
    if guess< session['number']:
        session['answer']='to low!'
        session['color']='red'
    elif guess> session['number']:
        session['answer']='to high!'
        session['color']='blue'
    else:
        session['answer']='correct'
        session['color']='green'
        
    print(session['answer'])
    print(f" number: {guess}, Answer: { session['number']},{session['answer']}")
    return redirect('/')
@app.route('/again',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
