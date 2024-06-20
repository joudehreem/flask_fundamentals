from flask import Flask, render_template, request
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
        print(request.form)
        strawberry=int(request.form['strawberry'])#
        raspberry=int(request.form['raspberry'])#
        apple=int(request.form['apple'])#
        first_name=request.form['first_name']#
        last_name=request.form['last_name']#
        student_id=request.form['student_id']#
        Customer_name=first_name+last_name
        count=strawberry+raspberry+apple
        print(f"Charging {Customer_name} for {count} fruits")#
        
        return render_template("checkout.html",strawberry=strawberry,raspberry=raspberry,apple=apple,first_name=first_name,last_name=last_name,student_id=student_id,Customer_name=Customer_name,count=count)



@app.route('/fruits')         
def fruits():
    images=[
    {'fruits_img':'apple.png','fruits_name':'Apple'},{'fruits_img':'blackberry.png','fruits_name':'Blackberry'},{'fruits_img':'raspberry.png','fruits_name':'Raspberry'},{'fruits_img':'strawberry.png','fruits_name':'Strawberry'},]
    return render_template("fruits.html",images=images)

if __name__=="__main__":   
    app.run(debug=True)    