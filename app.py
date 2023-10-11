from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return render_template('welcome.html')
        else:
            return render_template('index.html', error='Invalid credentials')
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
    
    