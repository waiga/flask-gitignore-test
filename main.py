from flask import Flask, render_template, request
from datetime import datetime
from secret_file import passwords

app = Flask(__name__)
current_time = datetime.now().strftime("%Y-%m-%d")

@app.route('/')
def home():
    return render_template('index.html', date=current_time)

@app.route('/login', methods=["POST"])
def receive_data():
    user_name=request.form['username']
    pass_word=request.form['password']
    return f"<h1>Name: {user_name}, Password: {pass_word}</h1>"

if __name__=='__main__':
    app.run(debug=True)