from statistics import quantiles
from database import get_db 
from fileinput import filename
from werkzeug.utils import secure_filename
import os
from fileinput import filename
import database
from flask import Flask,render_template,url_for,redirect,request

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
    con=get_db().cursor()
    con.execute(f"select * from customers where Customer_id=104 ;")
    cust=con.fetchone()
    con.close()
    
    
    
    return render_template('Educator_information.html',cust=cust)


@app.route('/quotations_pages')
def quotations_page() :
    con=get_db().cursor()
    con.execute(f"select * from Quotation ;")
    qutes=con.fetchall()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"select * from customers ORDER BY RANDOM() limit 1 ;")
    cust1=con.fetchall()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"select * from authors ORDER BY RANDOM() limit 1  ;")
    auth1=con.fetchall()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"select * from Sections_parts limit 8  ;")
    data1=con.fetchall()
    con.close()
    
    return render_template('quotations.html' , qutes=qutes , cust1=cust1 , auth1=auth1,data1=data1)

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

@app.route('/purchase_cart')
def purchase_cart() :
    return render_template('purchase_cart.html')

@app.route('/admin_pages' )
def admin_pages() :
    return render_template('admin_page.html' )

@app.route('/Latin_American_literature_translated')
def Latin_American_literature_translated() :
    con=get_db().cursor()
    con.execute("select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=6')
    rows=con.fetchall()
    con.close()
    return render_template('Latin_American_literature_translated.html',data=data ,rows=rows)




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
        con.close()
        if account:
        
            msg='Login Successfull in main page...!'
            return  redirect(url_for('home_pages')) 
           
        elif request.method == 'POST' and 'email_user' in request.form and 'password_user' in request.form:
          email_user = request.form['email_user']
          password_user = request.form['password_user']
          con=get_db().cursor()
          con.execute(f"SELECT * FROM admin  WHERE email = '{email_user}' AND password ='{password_user}'; ")
          account = con.fetchone()
          con.close()
            # Account doesnt exist or username/password incorrect
          if account :
            msg='Login Successfull in admin page Wellcome...!'
            return  redirect(url_for('admin_pages')) 
          else :
              msg = 'Incorrect username/password!' 
    return render_template('Login.html', msg=msg)
# **************************************************************
@app.route('/Translator_morality')
def Translator_morality() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=7')
    rows=con.fetchall()
    con.close()
    return render_template('Translator_morality.html',data=data ,rows=rows)
# ********************************************
@app.route('/Translated_childrens_literature')
def Translated_childrens_literature() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=8')
    rows=con.fetchall()
    con.close()
    return render_template('Translated_childrens_literature.html',data=data ,rows=rows)
#*********************************
@app.route('/Etiquette_of_difference_translated')
def Etiquette_of_difference_translated() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 7;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=9')
    rows=con.fetchall()
    con.close()
    return render_template('Etiquette_of_difference_translated.html',data=data ,rows=rows)
#*********************************
@app.route('/Esperanto_literature_translated')
def Esperanto_literature_translated() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 9;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=11')
    rows=con.fetchall()
    con.close()
    return render_template('Esperanto_literature_translated.html',data=data ,rows=rows)
#*********************************
@app.route('/X_ray')
def X_ray() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 9;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=12')
    rows=con.fetchall()
    con.close()
    return render_template('X_ray.html',data=data ,rows=rows)
#*********************************
@app.route('/Colors_and_their_meanings')
def Colors_and_their_meanings() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 9;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=13')
    rows=con.fetchall()
    con.close()
    return render_template('Colors_and_their_meanings.html',data=data ,rows=rows)
#*********************************
@app.route('/geology')
def geology() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 9;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=14')
    rows=con.fetchall()
    con.close()
    return render_template('geology.html',data=data ,rows=rows)
# ***************************************
@app.route('/Aerodynamics')
def Aerodynamics() :
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts limit 9;  ")
    data=con.fetchall()
    con.execute('select * from books where author_id=15')
    rows=con.fetchall()
    con.close()
    return render_template('Aerodynamics.html',data=data ,rows=rows)
#*********************************

@app.route("/Details_of_books/<int:id_book>",methods=("POST","GET"))
def Details_of_books(id_book) :
    con=get_db().cursor()
    con.execute(f"select * from books where book_id={id_book} ;")
    rows=con.fetchone()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"""select * from authors ORDER BY RANDOM() ;""")
    auth=con.fetchone()
    con.close()
  
    con=get_db().cursor()
    con.execute(f"""SELECT commont  , customer_name ,image_file
                FROM reviews  
                inner join Customers on  customer_id=reviews.id_cust
                ORDER BY RANDOM()
                 LIMIT 3 ;""")
    cust=con.fetchall()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"""select * from Quotation ORDER BY RANDOM() limit 3 ;""")
    quote=con.fetchall()
    con.close()
    return render_template("Details_books_2.html",rows=rows,auth=auth,cust=cust,quote=quote)

@app.route('/checkout_pages/<int:id_book>' ,methods=("POST" ,"GET"))
def checkout_page(id_book) :
    if request.method=="POST" :
        quantity=request.form['quantity_book']
        con=get_db()   
        con.execute(f"update books set quantity_book={quantity} where book_id={id_book};")

        con.commit()
        con.close()
        return redirect(url_for('checkout_page' ,id_book=id_book))  
    con=get_db().cursor()
    con.execute(f"select * from books where book_id={id_book}  ;")
    rows=con.fetchall()
    con.close()
    con=get_db().cursor()
    con.execute(f"select customer_name,number_visa ,cvv,visa_date from customers ORDER BY RANDOM()  ;")
    cust=con.fetchone()
    con.close()
    return render_template("checkout.html",rows=rows,cust=cust )  


# *************************************************************

@app.route('/authors_pages')
def authors_page() :
    conn=get_db().cursor()
    conn.execute("SELECT * FROM authors;") 
    rows = conn.fetchall()
    conn.close()
    
    conn=get_db().cursor()
    conn.execute("SELECT * FROM authors limit 4;") 
    data = conn.fetchall()
    conn.close()
    return render_template('pages_authors.html', rows=rows,data=data)


@app.route('/author_detlais/<int:id_author>' , methods=("POST" ,"GET"))
def author_detlais_ids(id_author):
    con=get_db().cursor()
    con.execute(f"select * from authors where authors.author_id={id_author} ;")
    auth=con.fetchone()
    con.close()
     
    con=get_db().cursor()
    con.execute(f"select * from books ORDER BY RANDOM() limit 4  ;")
    bks=con.fetchall()
    con.close()
    
    con=get_db().cursor()
    con.execute(f"select part_sections from Sections_parts  limit 5  ;")
    data=con.fetchall()
    con.close()
    return render_template('author_detials_new_2.html',auth=auth ,bks=bks,data=data)


# *************************************************





# *************************************************************************
@app.route("/home")
def home_page() :
    return render_template("Home.html")





# *************************************************************************


# ***************************************************************

@app.route("/manage_users")
def manage_user() :
    con=get_db().cursor()
    con.execute("select * from Customers ;")
    rows=con.fetchall()
    con.close()
    return render_template("Manage_users.html",rows=rows )

@app.route("/add_user" ,methods=("GET", "POST"))
def add_user() :
    if request.method=="POST" :
        customer_id=request.form['customer_id']
        customer_name=request.form['customer_name']
        country=request.form['country']
        age=int(request.form['age'])
        cust_year=request.form['cust_year']
        cust_month=request.form['cust_month']
        cust_day=request.form['cust_day']
        gender=request.form['gender']
        Number_visa=request.form['Number_visa']
        cvv=request.form['cvv']
        email=request.form['email']
        password_user=request.form['password_user']
        visa_date=request.form['visa_date']
        if 'image_file' not in request.files :
                # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['image_file']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
        
        con=get_db()
        con.execute(f"""insert into customers 
                    (customer_id,customer_name, country,age,cust_year,cust_month,cust_day,gender,Number_visa,cvv,email,password_user,visa_date,image_file)
                    values({customer_id},'{customer_name}','{country}',{age},{cust_year},{cust_month},{cust_day},'{gender}' ,{Number_visa},{cvv} ,'{email}','{password_user}' ,'{visa_date}' ,'{filename}')""")
        con.commit()
        con.close()
        return redirect(url_for('manage_user'))
    return render_template("add_user.html")

 
@app.route("/remove_user/<int:id_user_rr>/",methods=("GET" ,"POST"))
def remove_user(id_user_rr) :
    con=get_db()
    con.execute(f"delete from customers where customer_id={id_user_rr}")
    con.commit()
    con.close()   
    return redirect(url_for('manage_user'))

if __name__ == "__main__" :
    app.run ( debug =True)

@app.route("/update_user/<int:id_user>/" ,methods=["GET", "POST"])
def update_user(id_user) :
    if request.method=="POST" :
        customer_name=request.form['customer_name']
        country=request.form['country']
        age=int(request.form['age'])
        cust_year=request.form['cust_year']
        cust_month=request.form['cust_month']
        cust_day=request.form['cust_day']
        gender=request.form['gender']
        Number_visa=request.form['Number_visa']
        cvv=request.form['cvv']
        email=request.form['email']
        password_user=request.form['password_user']
        visa_date=request.form['visa_date']
        if 'image_file' not in request.files :
                # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['image_file']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
        con=get_db()
        con.execute(f"""update customers set
                    customer_name='{customer_name}', 
                    country='{country}', 
                    age={age},
                    cust_year = {cust_year},
                    cust_month={cust_month},
                    cust_day={cust_day},
                    gender='{gender}',
                    Number_visa={Number_visa},
                    cvv={cvv},
                    email='{email}',
                    password_user='{password_user}',
                    visa_date='{visa_date}',
                    image_file='{filename}'
                    where customer_id={id_user}""")
        con.commit()
        con.close()
        return redirect(url_for('manage_user'))
    con=get_db().cursor()
    con.execute(f"select * from customers where customer_id={id_user};")
    data=con.fetchone()
    con.close()   
    return render_template("update_user_page.html",data=data)


if __name__ == "__main__" :
    app.run ( debug =True)
# ***************************************************************************************
 
@app.route('/manage_books')
def manage_books() :
    con=get_db().cursor()
    con.execute(" select * from books ;")
    data2=con.fetchall()
    con.close()
    return render_template('manage_books.html', data2=data2)



@app.route("/addbook" ,methods=("GET" ,"POST"))
def add_book() :
    if request.method=="POST" :
        book_id=request.form['book_id']
        book_name=request.form['book_name']
        rate=int(request.form['rate'])
        book_date=request.form['book_date']
        price=float(request.form['price'])
        author_id=int(request.form['author_id'])
        quantity_book=int(request.form['quantity_book'])
      #uploade files
        if 'link' not in request.files :
            # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['link']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
      # insert to data base
        con=get_db()
        con.execute(f"""insert into books
                    (book_id,book_name ,rate, book_date ,price ,author_id,quantity_book,link)  
                    values('{book_id}' ,'{book_name}',{rate},'{book_date}', {price} ,{author_id} , {quantity_book}, '{filename}')""")
        con.commit()
        con.close()
        return redirect(url_for('manage_books'))
    return render_template("add_book.html")


@app.route("/updatebook/<int:id_book>" ,methods=("GET", "POST"))
def update_book_page(id_book) :
    if request.method=="POST" :
        book_name=request.form['book_name']
        rate=int(request.form['rate'])
        book_date=request.form['book_date']
        price=float(request.form['price'])
        author_id=int(request.form['author_id'])
        quantity_book=int(request.form['quantity_book'])
      #uploade files
        if 'link' not in request.files :
            # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['link']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
# insert to data base
        con=get_db()
        con.execute(f"""update books 
                    set book_name='{book_name}', 
                    price= {price},
                    rate ={rate},
                    book_date={book_date} ,
                    author_id='{author_id}' ,
                    quantity_book='{quantity_book}' 
                    where book_id={id_book} """)
        con.commit()
        con.close()
        return redirect(url_for('manage_books'))
    con=get_db().cursor()
    con.execute(f"select * from books where book_id={id_book};")
    data3=con.fetchone()
    con.close()   
    return render_template("update_book_page.html",data3=data3)

@app.route("/removebook/<int:id_book>")
def remove_book_page(id_book) :
    con=get_db()
    con.execute(f"delete from books where book_id={id_book}")
    con.commit()
    con.close()   
    return redirect(url_for('manage_books'))

# ****************************************************************


@app.route("/manage_author")
def manage_author() :
    con=get_db().cursor()
    con.execute("select * from authors ;")
    rows=con.fetchall()
    con.close()
    return render_template("Manage_authors.html",rows=rows )


@app.route("/addauthors" ,methods=("GET" ,"POST"))
def add_author() :
    if request.method=="POST" :
        author_id=request.form['author_id']
        name_author=request.form['name_author']
        rate=int(request.form['rate'])
        Description=request.form['Description']
        gender=(request.form['gender'])
        nationality=(request.form['nationality'])
      #uploade files
        if 'link_image' not in request.files :
            # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['link_image']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
      # insert to data base
        con=get_db()
        con.execute(f"""insert into authors
                    (author_id , name_author ,rate, Description ,gender ,nationality,link_image)  
                    values({author_id} , '{name_author}', {rate},'{Description}', '{gender}' ,'{nationality}' , '{filename}' )""")
        con.commit()
        con.close()
        return redirect(url_for('manage_author'))
    return render_template("add_author.html")



@app.route("/update_authors/<int:id_author>" , methods=("GET" ,"POST"))
def update_authors(id_author) :
    if request.method=="POST" :
        name_author=request.form['name_author']
        rate=int(request.form['rate'])
        Description=request.form['Description']
        gender=(request.form['gender'])
        nationality=(request.form['nationality'])
      #uploade files
        if 'link_image' not in request.files :
            # flash("there is no files") 
            return redirect(request.url)   
        file=request.files['link_image']
        filename=secure_filename(file.filename)   
        file.save(os.path.join('static', 'upload' ,filename))
        con=get_db()
        con.execute(f"""update authors set name_author='{name_author}' ,rate={rate},gender='{gender}', nationality='{nationality}', link_image='{filename}' where author_id={id_author} ;""")
        con.commit()
        con.close()
        return redirect(url_for('manage_author'))        
    con=get_db().cursor()
    con.execute(f"select * from authors where author_id={id_author} ;")    
    rows=con.fetchone()
    con.close()
    return render_template("update_authors_page.html", rows=rows)


@app.route("/remove_author_page/<int:id_author>")
def remove_author_page(id_author) :
    con=get_db()
    con.execute(f"delete from authors where author_id={id_author};")
    con.commit()
    con.close()   
    return redirect(url_for('manage_author'))




