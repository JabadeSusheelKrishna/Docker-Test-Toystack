from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Admin' and password == 'Admin':
            return "Hello World"
        else:
            return "Try Again"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
