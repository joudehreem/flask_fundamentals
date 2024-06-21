from flask import Flask,render_template,redirect,request,session
import random
from datetime import datetime


app=Flask(__name__)
app.secret_key='earn gold'

now = datetime.now() # current date and time
date_time = now.strftime("%Y/%m/%d, %I:%M %p")

@app.route('/')
def index():
  if 'gold' not in session:
    session['gold']=0
  if 'activities' not in session:
    session['activities'] = []
  return render_template('index.html',gold=session['gold'],activities=session['activities'] )

@app.route('/process_money', methods=['POST'])
def earn():
  print(request.form)
  building=request.form['building']

  if building=='farm':
    earn_gold=get_random(10, 20, "Farm")
  elif building =='cave':
    earn_gold=get_random(5, 10, "cave")
  elif building =='house':
    earn_gold=get_random(2, 5, "house")
  elif building =='casino':
    earn_gold=get_random(-50, 50, "casino")
  else:
    earn_gold=0
    print(earn_gold)
    print('casino') 
  session['gold']+=earn_gold
  
  if earn_gold >= 0:
        activity = f'Earned {earn_gold} golds from the {building}! ({date_time})'
  else:
        activity = f'Entered a {building} and lost {-earn_gold} golds...Ouch... ({date_time})'
  session['activities'].append(activity)
  print(activity)
  return redirect('/')

@app.route('/reset',methods=['POST'])
def restart():
  session.clear()
  return redirect('/')

def get_random(min, max, building):
  earn_gold = random.randint(min,max)
  print(earn_gold)
  print(building)
  return earn_gold

if __name__=="__main__":
  app.run(debug=True)