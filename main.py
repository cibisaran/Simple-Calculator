from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/sunny",methods=["POST"])
def operation():
    if (request.method=="POST"):
        first_name=request.json["firstname"]
        last_name=request.json["lastname"]
        result=f"my full name is : {first_name+last_name}"
    return jsonify(result)

@app.route("/via_postman",methods=["POST"])
def math_number_via_postman():
    if (request.method=="POST"):
        operation=request.json["operations"]
        num1=request.json["num1"]
        num2=request.json["num2"]
        if operation=="add":
            r=num1+num2
            result="the sub of two number will be" +" "+ str(r)
        elif operation=="substract":
            r=num1-num2
            result="the sub of two number will be" +" "+ str(r)
        elif operation=="multiply":
            r=num1*num2
            result="the sub of two number will be" +" "+ str(r)
        else:
            r=num1/num2
            result="the sub of two number will be" +" "+ str(r)

    return jsonify(result)
    
@app.route("/math",methods=["POST"])
def math_operation():
    if (request.method=="POST"):
        operation=request.form["operation"]
        num1=request.form["num1"]
        num2=request.form["num2"]
        if operation=="add":
            r=int(num1)+int(num2)
            result="the sub of two number will be" +" "+ str(r)
        elif operation=="substract":
            r=int(num1)-int(num2)
            result="the sub of two number will be" +" "+ str(r)
        elif operation=="multiply":
            r=int(num1)*int(num2)
            result="the sub of two number will be" +" "+ str(r)
        else:
            r=int(num1)/int(num2)
            result="the sub of two number will be" +" "+ str(r)

    return render_template('results.html',result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0")