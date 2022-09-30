from flask import Flask, render_template, redirect, session, request, flash
from server import app
from models.user import User

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
@app.route('/getby')
def getby():
    User.get_by(request.form['condition'])
@app.route('/delete/<id>')
def delete(id):
    User.delete_user(id)
    return(redirect('/read'))
@app.route('/update', methods = ['POST'])
def update():
    User.edit_user(fname = request.form['fname'], lname = request.form['lname'], email = request.form['email'], id = request.form['id'])
    return redirect('/read')
@app.route('/show/<id>')
def show (id):
    print(id)
    users = User.get_by(id)
    print(users)
    return(render_template('userinfo.html',users = users))
@app.route('/edit/<id>')
def edit(id):
    print(id + "all is good")
    users = User.get_by(id)
    return(render_template('/update.html', users = users))