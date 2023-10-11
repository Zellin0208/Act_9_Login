from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for("dashboard"))
        else:
            return render_template('index.html', error='Invalid credentials')
    else:
        return render_template('index.html')
        
@app.route("/dashboard")
def dashboard():
    return "Welcome to the dashboard!"
if __name__ == '__main__':
    app.run(debug=True)
