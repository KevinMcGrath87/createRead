from flask import Flask, request, redirect, session, render_template
from user import User
app = Flask(__name__)
app.secret_key = "allthelusers"

@app.route('/read')
def read():
    users = User.get_all()
    return(render_template('/read.html', users = users))
@app.route('/create')
def form():
    return(render_template('create.html'))
@app.route('/createUser', methods = ['POST'])
def createUser():
    User.insertion(request.form['first_name'],request.form['last_name'],request.form['email'])
    return(redirect('/read'))
if __name__ =='__main__':
    app.run(debug=True)