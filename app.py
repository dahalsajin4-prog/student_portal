from flask import Flask , render_template , request , redirect

app=Flask(__name__)

@app.route("/"  )
def login():
    return render_template("login.html")

@app.route("/submit" , methods=[ "POST" ])
def portal():
    username = request.form.get("username")
    password=request.form.get("password")

    if username=="sajin" and password=="pass":
        return render_template("index.html" , name=username)
    
    else:
        return render_template("login.html")

@app.route("/exam_form" )
def exam_form():
    return render_template("exam_form.html")

@app.route("/meeting" )
def meeting():
    return render_template("meeting.html")

@app.route("/Submit-Request" , methods=["POST"])
def request():
    return redirect("https://www.youtube.com/")
