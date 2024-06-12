from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def dojo_survey():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print('Got Post Info')
    name_from_form= request.form['name']
    location_from_form= request.form['location'] 
    favlang_from_form= request.form['favlang']  
    comment_from_form= request.form['comment']
    return render_template("result.html", name_on_template=name_from_form, location_on_template=location_from_form, favlang_on_template=favlang_from_form,comment_on_template=comment_from_form)

if __name__=="__main__":
    app.run(debug=True)