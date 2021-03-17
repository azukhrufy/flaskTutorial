from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)

list = ["Budi", "Hartono", "Eky", "Zahir", "Kokom"]

@app.route("/")
def home():
    return render_template("index.html", name = list)

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route("/<name>")
def user(name):
    return "Hello {}".format(name)

    
if __name__ == "__main__" :
    app.run()