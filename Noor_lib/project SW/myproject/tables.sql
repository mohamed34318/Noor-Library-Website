-- drop table Customers ;
-- create table Customers (
--   Customer_id int IDENTITY(100,1) NOT NULL UNIQUE PRIMARY KEY ,
--   customer_name varchar(255) ,
--   country char(100) ,
--   age int ,
--   cust_year YEAR ,
--   cust_month MONTH ,
--   cust_day day ,
--   gender char(50) ,
--   Number_visa Int ,
--   cvv int ,
--   email varchar(255),
--   password_user PASSWORD,
--   visa_date VARCHAR(255) ,
--   image_file text
-- ) ;

--  alter table books drop column link2;
-- -- alter table books add image_file VARCHAR(1000);
-- -- insert into Customers
-- --  values( 100, "mohamed" , "ahmed" , "nile" , 19 , 2000-1-22 , "male" , "C:\Users\ma510\OneDrive\Desktop\4998694.jpg",156324785642154 ,351,"22/1", "A person's appearance can be described in many ways. It is possible to tell about the person's style of clothing, manner of walking, colour and style of hair, facial appearance, body shape, and expression or even the person's way of talking.");
-- -- insert into Customers
-- --  values( 101, "saad" , "said" , "fayoum" , 25 , 2000-1-22 , "male" , "C:\Users\ma510\OneDrive\Desktop\4998694.jpg",15632432154 ,981,"20/2", "A person's appearance can be described in many ways. It is possible to tell about the person's style of clothing, manner of walking, colour and style of hair, facial appearance, body shape, and expression or even the person's way of talking.");
-- -- insert into Customers
-- --  values( 102, "ali" , "koshre" , "cairo" , 17 , 2000-1-22 , "male" , "C:\Users\ma510\OneDrive\Desktop\4998694.jpg",156324785642154 ,364,"16/5", "A person's appearance can be described in many ways. It is possible to tell about the person's style of clothing, manner of walking, colour and style of hair, facial appearance, body shape, and expression or even the person's way of talking.");
-- --  drop table books;
--  drop TABLE checkout;
DELETE FROM CUSTOMERS;

-- CREATE table checkout
--  ( book_name varchar(255) ,
--   link char(100) ,
--    rate int ,
--   book_date VARCHAR(255) ,
--    price float ,
--    check_id INT AUTO_INCREMENT NOT NULL UNIQUE
--    );
-- create table books (
--   Book_id int IDENTITY(1,1) not null UNIQUE  PRIMARY KEY ,
--   book_name varchar(255) ,
--   link char(100) ,
--   rate int ,
--   book_date VARCHAR(255) ,
--   price float ,
--   Description varchar(1000) ,
--   author_id int FOREIGNKEY REFERENCES Authors(author_id)
-- -- ) ;
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link2)
-- VALUES(132, "أدب أمريكا اللاتينية ", " ", 2," ",24," ",6," ");

-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(159,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4,"", 8," ",12," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(160,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4," ", 8," ",12," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(161,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4,"", 8," ",13," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(162,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4," ", 8," ",13," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(163,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4,"", 8," ",14," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(164,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4," ", 8," ",14," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(165,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4,"", 8," ",15," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(164,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4," ", 8," ",15," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(144,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",6," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(145,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",6," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(146,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",7," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(147,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",7," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(148,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",7," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(149,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",7," ");
-- insert into books (book_id , book_name ,link ,rate ,book_date ,price ,DESCRIPTION ,author_id, link_book)
-- VALUES(150,"1699كتاب مقدمة في علم الأخلاق مترجم" , " ", 4, " ",7," ",7," ");
-- -- ************************************************
-- --  -insert into books
-- --  values (100, "Oddities And Wonders Of The Peoples Of The World" , "https://www.noor-book.com/en/ebook-%D8%BA%D8%B1%D8%A7%D8%A6%D8%A8-%D9%88%D8%B9%D8%AC%D8%A7%D8%A6%D8%A8-%D8%B4%D8%B9%D9%88%D8%A8-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85-pdf" , 3 , " 24 Apr 2022 " ,20.5 ,"
-- --  عالمنا الكبير اليوم، يجمعه العديد من الطبائع والأديان والثقافات، ويفرقه أيضا العديد من الغرائب والعجائب والمعتقدات والعادات التي تبقى من الطرائف التي يطول الحديث عنها، فهي أحيانا غريبة وأحيانا طريفة، وأحيانا مقززة تقشعر لها الأبدان.
-- --  اشتمل هذا الكتاب على عدة فصول مختلفة، تناولت أخطر الكوارث الطبيعية كالزلازل والفياضانات، والبراكين والأعاصير والمجاعات في العالم، وأبرز العادات والتقاليد، والطبائع والعجائب. وأغرب الأحداث التي وقعت في تاريخ الأرض منذ آلاف السنين. والحديث عن أبشع الحروب الدموية في العالم، وأخطرها منذ بداية التاريخ. وعلى أغرب عادات الزواج عند القبائل البدائية والشعوب في مختلف القارات في العالم. كما تناول أغرب الأماكن الطبيعية، وكذلك المستحدثة على أيدي البشر منذ آلاف السنين حتى اليوم. ثم عرض ومناقشة أغرب ما جاء في أديان العالم،
-- --   منها الوثنية والسماوية، والنظريات الدينية القديمة، وأصحابها، وأهم معتقداتها. كما تم اعتماد أوثق وأصح المراجع العالمية والعربية، والمواقع الإلكترونية الرسمية من مصادرها الأولى، دون التعرض لذكرها،
-- --    تسهيلا للقارئ. وعدم إرهاق الحواشي بالنصوص",1);
-- -- insert into books
-- -- values (101, "فاتتي صلاه" , "file:///C:/Users/ma510/OneDrive/Desktop/swProject/pages/pages/home_and_detials_of_book/Details_of_books.html" , 4 , " 19 mar 2022 " ,19.5 ,"كتاب فاتتني صلاة  من تأليف الكاتب  اسلام جمال  كتاب موجه خاصة لمن لا يصلون و يتهاونون على الصلاة في هذا الكتاب سوف تجد أحسن الطرق للمواظبة عليها لأننا نعلم بأن الصلاة هي السبيل للسعادة و الطمأنينة..",1);
-- -- insert into books
-- -- values(102, "نظرية الفستق " , "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%86%D8%B8%D8%B1%D9%8A%D8%A9-%D8%A7%D9%84%D9%81%D8%B3%D8%AA%D9%82-pdf" , 2, " 10 Apr 2022 " ,10.5 ,"بذة عن كتاب نظرية الفستق
-- -- كتاب نظرية الفستق هو أحد كتب التنمية البشرية وتطوير الذات، مؤلف الكتاب هو فهد عامر الأحمدي،
-- --  يتكون الكتاب من جزئيين الجزء الأول يحتوي على 338 صفحة،
-- --   والذي يتضمن عدد كبير من المقالات التي تتحدث كيفية تطوير الذات وتحسين طرق التفكير وزيادة الوعي لدى الأشخاص.
-- -- والجزء الثاني يتكون من 332 صفحة، يتضمن 52 موضوعا في تطوير الذات وأخطاء التفكير وعلاقتنا مع الناس.",2);
-- -- insert into books
-- --  values(103, "" , "" , 3 , " 24 Apr 2022 " ,20.5 ,"كتاب - الجامع المسند الصحيح المختصر من أُمور رسول الله صلى الله عليه وسلّم وسننه وأيامه - الشهير باسم
-- --  - صحيح البخاري - صنفه الإمام محمد بن إسماعيل البخاري .
-- -- هو أبرز كتب الحديث النبوي عند المسلمين من أهل السنة والجماعة.",3);
-- -- insert into books
-- -- values(104, "صحيح البخاري" , "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A-pdf" , 3 , " 24 Apr 2022 " ,20.5 ,"كتاب - الجامع المسند الصحيح المختصر من أُمور رسول الله صلى الله عليه وسلّم وسننه وأيامه
-- -- - الشهير باسم - صحيح البخاري - صنفه الإمام محمد بن إسماعيل البخاري .
-- -- هو أبرز كتب الحديث النبوي عند المسلمين من أهل السنة والجماعة.",4);
-- -- insert into books
-- -- values(105, "القران الكريم " , "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%AA%D8%B5%D9%81%D8%AD-%D8%A7%D9%84%D9%82%D8%B1%D8%A7%D9%86-%D8%A7%D9%84%D9%83%D8%B1%D9%8A%D9%85-pdf" , 3 , " 24 Apr 2022 " ,20.5 ,"لقرآن، ويُسمّى تكريمًا القرآن الكريم، هو كتاب الله المعجز عند المسلمين، يُعَظِّمُونه ويؤمنون بأنّه كلام الله، وبأنه قد أُنزل على محمد بن عبد الله للبيان والإعجاز، وبأنه محفوظ في الصدور والسطور من كل مس أو تحريف، وبأنه منقولٌ بالتواتر، وبأنه المتعبد بتلاوته، وبأنه آخر الكتب السماوية
-- --  بعد صحف إبراهيم والزبور والتوراة والإنجيل.
-- -- ",4);
-- -- insert into books
-- --  values(106, "مناهج البحث العلمي" , "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%85%D9%86%D8%A7%D9%87%D8%AC-%D8%A7%D9%84%D8%A8%D8%AD%D8%AB-%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A-pdf-1587054532" , 3 , " 24 Apr 2022 " ,20.5 ,"يتحدث الكتاب عن طبيعة البحث العلمي وما يتعلق به من مفاهيم كتعريف المعرفة والعلم، والتفريق بينهما، وتعريف البحث العلمي، وخصائصه، وأهدافه، كما يتحدث عن أنواع البحوث العلمية ومناهجها،
-- -- ويتحدث أيضا عن خطة البحث العلمي، وخطوات إعدادها، وتضمن أيضا الحديث عن أدوات جمع البيانات والمعلومات، سواء كانت نظرية أم تطبيقية، فكما وتناول الحديث عن المكتبة الإلكترونية والأنترنت ودورهما في خدمة البحث العلمي، وتضمن الحديث عن آليات كتابة تقرير البحث
-- -- ، وأخيراً تناول منهجية تحقيق المخطوطات.",2);
-- -- insert into books values(107, "فن التعامل مع الناس " , "https://www.noor-book.com/%D9%83%D8%AA%D8%A7%D8%A8-%D9%81%D9%86-%D8%A7%D9%84%D8%AA%D8%B9%D8%A7%D9%85%D9%84-%D9%85%D8%B9-%D8%A7%D9%84%D9%86%D8%A7%D8%B3-pdf" , 3 , " 24 Apr 2022 " ,20.5 ,"صاحب الظل الطويل أو أبي طويل الساقين، هي رواية للكاتبة الأمريكية جين ويبستر. تدور أحداث القصة حول فتاة يتيمة اسمها جودي أبوت، التي تحصل على منحة للدراسة في مدرسة لينكولن الثانوية من قبل شخص لا تعرفه، اسمه المستعار
-- --  هو جون سميث وقد ابتكرت له اسم ة.",6);

-- *************************************************************************
-- create table Read_buy_books (
--   id_books int FOREIGNKEY REFERENCES books(book_id) ,
--   id_customers int FOREIGNKEY REFERENCES Customers(customer_id) ,
--   CONSTRAINT PK_Person_read PRIMARY KEY (id_books,id_customers)
-- ) ;

-- -- insert into Read_buy_books values (100 , 100);
-- -- insert into Read_buy_books values (101 , 101);
-- -- insert into Read_buy_books values (103 , 103);
-- -- insert into Read_buy_books values (104 , 104);
-- -- insert into Read_buy_books values (105 , 105);
-- -- insert into Read_buy_books values (106 , 106);
-- -- insert into Read_buy_books values (107 , 107);

-- create table has_books (
--   id_books int FOREIGNKEY REFERENCES Sections(book_id) ,
--   id_sec int FOREIGNKEY REFERENCES Customers(sec_i) ,
--   CONSTRAINT PK_Person_read PRIMARY KEY (id_books,id_sec)
-- ) ;

-- -- insert into has_books values ( 100, 100  );
-- -- insert into has_books values ( 101, 100  );
-- -- insert into has_books values ( 103, 100  );
-- -- insert into has_books values ( 104, 101  );
-- -- insert into has_books values ( 105, 101  );
-- -- insert into has_books values ( 106, 102  );
-- -- insert into has_books values ( 107, 103  );



-- create table Sections (
-- sec_id int IDENTITY(100,1) NOT NULL unique  PRIMARY KEY ,
-- sect_name varchar(255) NOT NULL
-- );
-- insert into Sections values (100 , "الدين الإسلامي والعلوم الشرعية" );
-- insert into Sections values (101 , "الأدب العالمي والأدب المترجم" );
-- insert into Sections values (102 , " العلوم العامة والعلوم الطبيعية");
-- insert into Sections values (103 ,"لغات وتقنيات برمجة الحاسوب " );
-- insert into Sections values (104 ,"الهندسة والعلوم الهندسية" );

-- create table Sections_parts(
-- id_sec int FOREIGNKEY REFERENCES Customers(sec_i),
-- sect_name varchar(255) NOT NULL,
-- part_sections varchar(255) not null

-- );

-- -- insert into Sections_parts values (100 , "الدين الإسلامي والعلوم الشرعية","آداب وأخلاق إسلامية" );
-- -- insert into Sections_parts values (100 , "الدين الإسلامي والعلوم الشرعية","أبو حنيفة النعمان" );
-- -- insert into Sections_parts values (100 , "الدين الإسلامي والعلوم الشرعية","أبو هريرة" );
-- -- insert into Sections_parts values (100 , "الدين الإسلامي والعلوم الشرعية","أحاديث الأحكام" );
-- -- insert into Sections_parts values (100 , "الدين الإسلامي والعلوم الشرعية","أحكام الجهاد فى الإسلام" );

-- -- insert into Sections_parts values (101 , "الأدب العالمي والأدب المترجم","أدب أمريكا اللاتينية مترجم" );
-- -- insert into Sections_parts values (101 , "الأدب العالمي والأدب المترجم"," أدب الأخلاق مترجم" );
-- -- insert into Sections_parts values (101 , "الأدب العالمي والأدب المترجم","أدب الأطفال مترجم" );
-- -- insert into Sections_parts values (101 , "الأدب العالمي والأدب المترجم","أدب الإختلاف مترجم" );
-- -- insert into Sections_parts values (101 , "الأدب العالمي والأدب المترجم","أدب الإسبيرانتو مترجم" );

-- -- insert into Sections_parts values (102 , " العلوم العامة والعلوم الطبيعية", "الأشعة السينية ");
-- -- insert into Sections_parts values (102 , " العلوم العامة والعلوم الطبيعية", " الألوان ودلالاتها");
-- -- insert into Sections_parts values (102 , " العلوم العامة والعلوم الطبيعية", "الجيولوجيا ");
-- -- insert into Sections_parts values (102 , " العلوم العامة والعلوم الطبيعية", " الديناميكا الهوائية");
-- -- insert into Sections_parts values (102 , " العلوم العامة والعلوم الطبيعية", "العلوم البحتة ");

-- -- insert into Sections_parts values (103 ,"لغات وتقنيات برمجة الحاسوب ", " لغة البرمجة السي شارب #C" );
-- -- insert into Sections_parts values (103 ,"لغات وتقنيات برمجة الحاسوب ", "لغة البرمجة جافا Java " );
-- -- insert into Sections_parts values (103 ,"لغات وتقنيات برمجة الحاسوب ", "لغة برمجة أتش تى أم أل HTML " );
-- -- insert into Sections_parts values (103 ,"لغات وتقنيات برمجة الحاسوب ", "لغة برمجة بايثون Python " );
-- -- insert into Sections_parts values (103 ,"لغات وتقنيات برمجة الحاسوب ", " لغة برمجة سي بلس بلس C++" );

-- -- insert into Sections_parts values (104 ,"الهندسة والعلوم الهندسية" , "الأدوات الهندسية ");
-- -- insert into Sections_parts values (104 ,"الهندسة والعلوم الهندسية" , "المضخات ");
-- -- insert into Sections_parts values (104 ,"الهندسة والعلوم الهندسية" , " هندسة أنظمة الآلات");
-- -- insert into Sections_parts values (104 ,"الهندسة والعلوم الهندسية" , "هندسة الآلات الزراعية ");
-- -- insert into Sections_parts values (104 ,"الهندسة والعلوم الهندسية" , "هندسة الأنهار ");



-- create table authors (
--   author_id int IDENTITY(1,1) unique not null primary key,
--   name_author char(100) ,
--   rate int ,
--   Description varchar(1000) ,
--   gender char(50) ,
--   nationality char(100) ,
--   AdminSSN  int FOREIGNKEY REFERENCES Admin (AdminSSN)
-- ) ;



-- create table Quotation (
--   Writer_Name varchar(255),
--   Book_Name varchar(255),
--   Book_Link varchar(1000),
--   Quato varchar(4500) ,
--   Cust_id int FOREIGNKEY REFERENCES Customers(customer_id)
-- ) ;

-- insert into Quotation values ("mohamed" , "هو كلام الله", "Oddities And Wonders Of The Peoples Of The World", "Oddities And Wonders Of The Peoples Of The Worlddfqwfqwfqwfwfqw wqw "
-- ,100);

-- create table reviews (
--   Writer_Name varchar(255),
--   Book_Name varchar(255),
--   Book_Link varchar(1000),
--   commont varchar(4500) ,
--   Cust_id int FOREIGNKEY REFERENCES Customers(customer_id)
--  ) ;

-- insert into reviews values ("mohamed" , "هو كلام الله", "Oddities And Wonders Of The Peoples Of The World", "Oddities And Wonders Of The Peoples Of The Worlddfqwfqwfqwfwfqw wqw "
-- ,100)

-- create table Admin (
--   AdminSSN int identity(200,1) unique not null primary key,
--   name_admin char(100) ,
--   DOB date,
--   gender char(50),
--   BookID int FOREIGNKEY REFERENCES books(book_id)
--   email varchar(255) ,
--   password varchar(255)
-- ) ;