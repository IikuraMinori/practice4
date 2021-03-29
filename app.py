from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/salary")
def top():
    time = request.args.get("time")
    money = request.args.get("money")
    salary = int(time) * int(money)
    return render_template("salary_result.html",salary=salary)    
    
@app.route("/circle")
def top2():
    r = request.args.get("r")
    pi = 3.14
    area = pi * int(r)
    cir = 2 * pi * int(r)
    return render_template("circle.html",area = area, cir = cir)

if __name__ == "__main__" :
    app.run(debug=True) 
