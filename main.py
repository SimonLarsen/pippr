from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
import pippr

app = Flask(__name__)
app.secret_key = "M4gyf4xnYLaLM8Cn"

def add_names(pips):
    for pip in pips:
        pip["name"] = pippr.get_name(pip["username"])
    return pips

@app.route("/")
def index():
    if "username" in session:
        pips = add_names(pippr.get_recent_pips(20)[::-1])
        return render_template("timeline.html", pips=pips)
    else:
        return render_template("login.html", error=request.args.get("error"))

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if pippr.check_user(username, password):
        session["username"] = username
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index", error="login"))

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
    else:
        return redirect(url_for("index", error="register"))

@app.route("/post", methods=["POST"])
def post():
    username = session["username"]
    text = request.form["text"]

    pippr.post_pip(username, text)
    if "from_user" in request.form:
        return redirect(url_for("userpage", username=request.form["from_user"]))
    else:
        return redirect(url_for("index"))

@app.route("/profile")
def profile():
    username = session["username"]
    return redirect(url_for("userpage", username=username))

@app.route("/mentions")
def mentions():
    username = session["username"]
    pips = add_names(pippr.get_mentions(username)[::-1])
    return render_template("mentions.html", username=username, pips=pips)

@app.route("/user/<username>")
def userpage(username):
    pips = add_names(pippr.get_user_pips(username)[::-1])
    name = pippr.get_name(username)
    return render_template("user.html", username=username, name=name, pips=pips)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    pips = add_names(pippr.search_pips(query)[::-1])
    return render_template("search.html", query=query, pips=pips)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
