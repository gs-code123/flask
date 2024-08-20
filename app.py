from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
print("app.py", __name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/center", defaults = {"name": "home"})
@app.route("/center/<name>")
def center(name):
    if name == "home": 
        return render_template("center.html")
    else:
        return render_template("center.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

# @app.route("/center/jaipur")
# def jaipur_center():
#     return "<h1> Welcome to jaipur center page </h1>"

if __name__ == "__main__":
    app.run(debug = True)