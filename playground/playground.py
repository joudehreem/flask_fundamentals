from flask import Flask, render_template
app=Flask(__name__)

@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<color>')
def playground(x=3, color="blue"):
  return render_template('playground.html',header='Welcome!',box=x,color=color,title='PlayGround')

if __name__=="__main__":
    app.run(debug=True)
