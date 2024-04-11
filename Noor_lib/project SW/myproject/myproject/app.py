from statistics import quantiles
from database import get_db 
from fileinput import filename
from werkzeug.utils import secure_filename
import os
from fileinput import filename
import database
from flask import Flask,render_template,url_for,redirect,request
from flask import Flask, flash, render_template, request, redirect, session, url_for
import sqlite3 
from flask import request, redirect
from flask import url_for


app=Flask(__name__)


@app.route("/")
def home_pages() :
    con=get_db().cursor()
    con.execute("select * from books ;")
    rows=con.fetchall()
    con.execute("""SELECT Sections_parts.part_sections as name_parts
                FROM Sections_parts
                INNER JOIN Sections ON Sections_parts.id_sec=Sections.sec_id
                 LIMIT 9; """)
    rows2=con.fetchall();
    print(rows)
    con.close()
    return render_template("home_page.html",rows=rows ,rows2=rows2)



@app.route("/view_page")
def view_books() :
    return render_template('view_page.html')


@app.post("/search")
def search_book() :
    name=request.form['search']
    con=get_db().cursor()
    con.execute(f"select * from books where book_name like '%{name}%' ")
    data=con.fetchall()
    con.close()
    return render_template("home_page.html",rows=data)

@app.route('/user_info')
def user_informations() :
    return render_template('Educator_information.html')


# @app.route('/login')
# def login_page() :
#     return render_template('Login.html')

@app.route('/authors_pages')
def authors_page() :
    return render_template('pages_authors.html')

@app.route('/quotations_pages')
def quotations_page() :
    return render_template('quotations.html')

@app.route('/Educated_communitys')
def Educated_community() :
    return render_template('Educated_community.html')

@app.route('/reviews_pages')
def reviews_page() :
    return render_template('Book_Reiews.html')

@app.route('/page_sections_view')
def sections_page() :
    con=get_db().cursor()
    con.execute(f" select  Sections.sect_name from Sections where sec_id=100 ;")
    one=con.fetchone()
    con.close()

    con=get_db().cursor()
    con.execute(f" select  Sections.sect_name from Sections  where sec_id=101 ;")
    two=con.fetchone()
    con.close()

    con=get_db().cursor()
    con.execute(f" select  Sections.sect_name from Sections  where sec_id=102 ;")
    three=con.fetchone()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"""select part_sections 
                 FROM Sections_parts 
                 where id_sec =100; """)
    d1=con.fetchall()
    con.close()   
           
    con=get_db().cursor()
    con.execute(f"""select part_sections 
                 FROM Sections_parts 
                 where id_sec =101; """)
    d2=con.fetchall()
    con.close()   
           
    con=get_db().cursor()
    con.execute(f"""select part_sections 
                 FROM Sections_parts 
                 where id_sec =102; """)
    d3=con.fetchall()
    con.close()          
    
    return render_template('page_sections.html', one=one, two=two ,three=three , d1=d1, d2=d2, d3=d3)
    

@app.route('/polite_america_tranlated')
def polite_america_tranlated() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=1')
    rows=con.fetchall()
    con.close()
    return render_template('polite_america_tranlated.html',data=data ,rows=rows)

@app.route('/Abu_Hanifa_al_Numan')
def Abu_Hanifa_al_Numan() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=2')
    rows=con.fetchall()
    con.close()
    return render_template('Abu_Hanifa_al_Numan.html',data=data ,rows=rows)

@app.route('/Abu_Hurairah')
def Abu_Hurairah() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=3')
    rows=con.fetchall()
    con.close()
    return render_template('Abu_Hurairah.html',data=data ,rows=rows)


@app.route('/Hadiths_of_Judgments')
def Hadiths_of_Judgments() :
    con=get_db().cursor()
    con.execute("select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=4')
    rows=con.fetchall()
    con.close()
    return render_template('Hadiths_of_Judgments.html',data=data ,rows=rows)


@app.route('/The_provisions_of_jihad_in_Islam')
def The_provisions_of_jihad_in_Islam() :
    con=get_db().cursor()
    con.execute("select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=5')
    rows=con.fetchall()
    con.close()
    return render_template('The_provisions_of_jihad_in_Islam.html',data=data ,rows=rows)

@app.route('/Details_of_books')
def Details_of_book() :
    return render_template('Details_of_books.html')

@app.route('/purchase_cart')
def purchase_cart() :
    return render_template('purchase_cart.html')

@app.route('/admin_pages')
def admin_pages() :
    return render_template('admin_page.html')

@app.route('/Latin_American_literature_translated')
def Latin_American_literature_translated() :
    con=get_db().cursor()
    con.execute("select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=6')
    rows=con.fetchall()
    con.close()
    return render_template('Latin_American_literature_translated.html',data=data ,rows=rows)


@app.route('/manage_books')
def manage_book() :
    con=get_db().cursor()
    con.execute(" select * from books limit 16;")
    rows=con.fetchall()
    con.close()
    return render_template('manage_books.html', rows=rows)


@app.route('/manage_users')
def manage_users() :
    con=get_db().cursor()
    con.execute(" select * from Customers ;")
    rows=con.fetchall()
    con.close()
    return render_template('Manage_users.html', rows=rows)

@app.route('/manage_author')
def manage_authors() :
        return render_template('Manage_authors.html')


# ******************************************************

@app.route("/Sgin_up", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if (request.form.get('email') !="" and request.form.get('password_user') !="") :
            customer_name=request.form['customer_name']
            country=request.form['country']
            age=int(request.form['age'])
            cust_year = request.form['year']
            cust_month = request.form['month']
            cust_day = request.form['day']
            gender=request.form['gender']
            email=request.form['email']
            Number_visa=request.form['num_visa']
            cvv=request.form['cvv']
            visa_date=request.form['visa_date']
            password_user=request.form['password_user']
            con=get_db()
            count=100
            count+=1
            con.execute(f"""insert into customers
                        (Customer_id,customer_name, country,age,cust_year,cust_month,cust_day,gender,email,Number_visa,cvv,visa_date,password_user)
                        values({count},'{customer_name}', '{country}',{age},'{cust_year}','{cust_month}','{cust_day}','{gender}','{email}',{Number_visa},{cvv},'{visa_date}','{password_user}');""")
            con.commit()
            con.close()
            
        return redirect (url_for('login_page'))
    return render_template('Sgin_up.html')    


# ****************************************************

@app.route("/login_page",methods=['GET','POST'])
def login_page():
    msg=''
    if request.method == 'POST' and 'email_user' in request.form and 'password_user' in request.form:
        # Create variables for easy access
        email_user = request.form['email_user']
        password_user = request.form['password_user']
        con=get_db().cursor()
        con.execute(f"SELECT * FROM Customers WHERE email = '{email_user}' AND password_user ='{password_user}' ")
        account = con.fetchone()
        # If account exists in accounts table in our database
        if account:
            msg='Login Successfull...!'
            return  redirect(url_for('home_pages'))
           
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('Login.html', msg=msg)