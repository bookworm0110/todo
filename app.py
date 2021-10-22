import psycopg2
from dbconn import create
from flask import Flask, render_template, redirect, request
import requests
import sqlite3
app = Flask(__name__)
dbf = r"/Users/plasma/Documents/Code/docs/todo.db"
@app.route("/")
def home():
    connection=create(dbf)
    connection.row_factory=sqlite3.Row
    cur=connection.cursor()
    cur.execute("SELECT * FROM todos")
    rows=cur.fetchall()
    # list_=[]
    # for i in rows:
    #     todo=i['name'], i['id']
    #     list_.append(todo)
    return render_template('todo.html',list=rows)
@app.route("/new",methods=['POST'])
def new():
    form=request.form.get('name')
    connection=create(dbf)
    cur=connection.cursor()
    cur.execute('INSERT INTO todos (name)VALUES(?)',(form,))
    connection.commit()
    return redirect("/")
@app.route("/complete/<int:id>")
def complete(id):
    connection=create(dbf)
    connection.row_factory=sqlite3.Row
    cur=connection.cursor()
    cur.execute("DELETE from todos WHERE id=?", (str(id),))
    connection.commit()
    return redirect("/")