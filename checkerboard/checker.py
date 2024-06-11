from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')

def checker_board(x=3,y=3):
    return render_template('index.html',title='CheckerBoard',x=x,y=y, )

if __name__=='__main__':
    app.run(debug=True, port=9000)




