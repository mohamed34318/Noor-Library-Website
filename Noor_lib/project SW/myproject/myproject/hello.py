
from flask import Flask, flash, render_template, request, redirect, session, url_for
import sqlite3 
from flask import request, redirect
from flask import url_for


app = Flask(__name__)
app.secret_key = "123"


@app.route("/login",methods=['GET','POST'])
def login() :
    if request.method=='POST' : 
        
        conn=sqlite3.connect('tables.sql')
        cursor=conn.cursor()
        
        Email=request.form.get('Email')
        Password=request.form.get('Password')
        
        query="SELECT *FROM users WHERE  Email= '"+Email+"' and Password='"+Password+"' "
        results=cursor.fetchall()
        
        if len(results)==0 :
            flash("Email and Password Mismatch","danger")
            return render_template("login.html")
        else :
            return render_template("mainpage.html")
        
    return render_template("login.html")


@app.route("/",methods=['GET','POST'])
@app.route("/Sgin up.html", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        conn=sqlite3.connect('tables.sql')
        if(request.form.get('Name')!=""and request.form.get('Password')!=""):
            name = request.form.get('Name')
            password = request.form.get('Password')
            email = request.form.get('Email')
            
            Gender =request.form.get('Gender')
            request.form.get('Gender')
            day = request.form.get('Day')
            month = request.form.get('Month')
            year = request.form.get('Year')
            
        conn.execute(f"""INSERT INTO users 
        (Name,Password,Email,Gender,Day,Year,Month)
        VALUES
        ('{name}','{password}','{email}','{Gender}','{day}','{month}','{year}');""")

        conn.commit()
        conn.close()
        return redirect (url_for("login"))
    return render_template('Sgin up.html')