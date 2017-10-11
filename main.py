from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
import pippr

app = Flask(__name__)
app.secret_key = "M4gyf4xnYLaLM8Cn"

def prepare_pips(pips):
    out = []
    for pip in pips:
        t = pip.copy()
        t["name"] = pippr.get_name(t["username"])
        out.append(t)
    return out

@app.route("/")
def index():
    if "username" in session:
        pips = prepare_pips(pippr.get_recent_pips(20))
        return render_template("timeline.html", pips=pips)
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if pippr.check_user(username, password):
        session["username"] = username
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    name = request.form["name"]
    password = request.form["password"]
    if pippr.register_user(username, name, password):
        session["username"] = username
    return redirect(url_for("index"))

@app.route("/post", methods=["POST"])
def post():
    username = session["username"]
    text = request.form["text"]

    pippr.post_pip(username, text)
    return redirect(url_for("index"))

@app.route("/profile")
def profile():
    username = session["username"]
    return redirect("/user/" + username)

@app.route("/user/<username>")
def userpage(username):
    pips = prepare_pips(pippr.get_user_pips(username))
    name = pippr.get_name(username)
    return render_template("user.html", username=username, name=name, pips=pips)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    pips = prepare_pips(pippr.search_pips(query))
    return render_template("search.html", query=query, pips=pips)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
