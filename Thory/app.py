from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# homepage login page
@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-Valid Credentials. Try again", mimetype="text/plain") #text/html
        
    return """
        <h2>Login Page</h2>
            <form>
                method = "POST"
                Username: <input type="text" name="username"> <br>
                Password: <input type="text" name="password"> <br>
                <input type="submit" value="Login">
            </form>
    """

# welecome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a hred={url_for("logout")}>Logout</a>
    '''
    return redirect(url_for("login"))

# logout 
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


app.run(debug=True)
