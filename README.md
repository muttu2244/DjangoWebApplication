# DjangoWebApplication

https://www.youtube.com/watch?v=OTmQOjsl0eg&ab_channel=Telusko



Create Virtual Env
Install django
Create "Applications" FOlder 
cd into "Application" Folder
Run "django-admin startproject FirstWebAppl"
   It contains "manage.py" file (to manage the project)
   It contains "FirstWebAppl" folder which contains
            __init__.py
            asgi.py
            settings.py     (for settings)
                    SecretKey (used in deployment)
                    debug = true (gives lot of information, make it false before deployment)
                    middleware (for security purpose)
                    templates == django templates (DTL-- Django template language)
                    databases = default (sqllite), we can use any DB
                    
            urls.py     (FOR all URLS, by default it will have only "admin/")
            wsgi.py     (For deployment)
            
Run "python manage.py runserver" to start a default webapplication
Note: Works on MVT (Model , View , Template ) architecture


 TO CREATE ACTUAL APP , WE HAVE TO CREATE ONE
 
 Run "python manage.py startapp Yogi" (a Folder with "Yogi" is created )
 Yogi folder contains following
        "Migrations" folder
        __init__.py file
        admin.py file
        apps.py file
        models.py file  (Related to the DB)
        tests.py file   (Related to the Testcases)
        views.py file   (Related to the Function definitions for each Endpoints (URL))
        
  Note:
    The moment you request for the "http://127.0.0.1:8000/" it searches the app specific urls.py (ex: "/home", "/search", "/payment" etc)
    But "FirstWebAppl\urls.py " is for the global project and not for the particular app... 
    Therefore every app should have its own "urls.py" (ex: Yogi\urls.py)... so create a "urls.py" in the "Yogi" folder (App)
        urls.py file    (Related to the URLS for the YOGI app )
        Add these lines in "urls.py"
        
            """ 
            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.home, name='home'),          #For Home   "views.home" is a "home" function in the views.py file
                path('add',views.add,name='add'),           #For add URL "views.add" is a "add" function in the views.py file
                    ]
            """
    whatever changes you make in "Yogi\urls.py" it should also be updated in the " FirstWebAppl\urls.py "            
     
     
For beutification of the HTML contents we have to use either DTL(Django Templates Language ) or Jinga Templates for that.. 

Create a "templates" folder and 
   create "base.html"  
   Create "home.html" and extend it with "base.html"      
                    
Once the html pages are created in views.py, we should use "render" the html page based on the request, instead of "HttpResponse"    

HTTPMETHODS

using POST method instead of GET (default): go to "home.html" and add "method=POST" after the "action = add"
Add "{% csrf_token %}  " which is from the default security features provided in the "MIDDLEWARE" in "settings.py"

Change the method from GET to POST in the "views.py" as well
So, now the address bar will not have the information of TWO numbers etc... otherwise which is a security threat ...
The information will now be handled using cookies, it wont store it on the address bar


Architecture
                                                                        --------- Model ------ > Database
                                                                       | 
User ------ > Django FW ------ > URL ---------- > View --------------> |
                                                                       |
                                                                       ----------- Template --- (DTL / Jinga Templates ) (HTML Templates)
                                                                       
                                                                       
                                                                       
                                                                       
MVT VS MVC 

Model --- Model 
Template --- View
View ----- Controller




DOWNLOAD "Tavello colorlib" free template for building websites

Create a New APP, called "TOUR" Run cmd (python manage.py startapp Tour)

copy all the *.html files from "Travello Colorlib" template and place it into templates folder

Create "urls.py" in Tour App and copy paste every thing as that of Yogi app 
and make necessary changes into "Tour/urls.py"
make necessary changes in the main urls file that is "FirstWebAppl/urls.py"

Make changes to the "Tour/Views.py" as applicable 

        
Run the server (python manage.py runserver)

Create a folder called as "static" in the Applications folder
put all the "Travello Colorlib" subfolders ("images', "js", "plugin", "styles") etc to the "static" foldre

In "settings.py" add as follows
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') (This is the place where all the static files are present)
    
django will pick all the above static files and puts them into its own folder ex: assets, we have to add the following lines
    
   STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
   
Run "python manage.py collectstatic" (all the static files will be copied to "assets")
    "257 static files copied to 'D:\Miscellaneous\DjangoWebApplication\Applications\assets'."
    

Make changes to "index.html" in ALL the places where it refers to "images", "js", "plugins", "styles"
    and change it to refer from the static folder
    
    EX: 
    change from "href="styles/bootstrap4/bootstrap.min.css" to   
        href="{ % static 'styles/bootstrap4/bootstrap.min.css' %}"          
        
   Add "{% load static %}" at the top of "index.html"
   
   
   
Making the Content DYNAMIC 

    Remove 5 destinations out of 6, from "index.html"
    
    Each destination(Object) has 4 attributes (Image, Name, Description , Price)
    
    In "models.py" create a class called "Destination" with 4 attributes as above 
    In "views.py" create as many objects as you want for the "Destination Class" with initializing each of the above attributes 
    
    Make a list of all the objects 
      and render that list of objects whenever index.html is called
    
    In index.html use a for loop to access all the objects (No matter how many objects) ---- Number of cities can also be dynamic 
            There can be 10 / 20 / 100 cities (any no of cities) 
            
     use "{% for dest in dests %} "  and "{% endfor %}"  for using the for loop and
        change the price to "dest.price" 
        change the desc to  "dest.desc"
        change the name to "dest.name" 
       
      but for image we have to add the following at the top
            " {% static "images" as baseURL %} " 
       and change it from 
            src="{% static 'images/destination_1.img' %}" 
                        TO 
            src="{{baseURL}}/{{ dest.img }}" -------------------- > 2 jinga variables seperated
        
        Using If - Else block in html
            add one more field in models.py which is "offer: bool" (bool is True/False)
            In views.py ... add this field for each object, and make it True only for the object which you want
            In index.html use if-else block as follows
                {% if dest.offer %}    and   {% endif %}



WORKING WITH DATABASE

    ORM ---- Object relational mapping
    
    When we create a class "class Customer" with attribute
                cust_id, cust_name, cust_add, cust_phone ... 
         
    ORM will automatically creates a Customer Table in the DB 
        and it will also automatically creates 4 fields in that table 
        
    Now if i create 5 Objects / instances of Customer Class
    ORM will automatically create 5 ROWS in the Customer Table ...
    
    The more no of objects you create, the more no of ROWS will get added automatically by ORM
    
    Download POSTGRES from  "https://www.enterprisedb.com/downloads/postgres-postgresql-downloads"
    
    We also need the UI interface for POSTGRES DB... 
    
    Download PGAdmin UI from "https://www.pgadmin.org/download/pgadmin-4-windows/" (Postgres management tool)
    
    Create a DB by name "FirstWebApplDB" in the PGAdmin UI
    
    In Settings.py change the 
        Engine to postgresql from sqlite3
        Name to "FirstWebApplDB"  (DB Name) 
        Add USER as 'postgres'
        Add PWD as '2244'
        Add HOST as 'localhost'
        
        
     Install 'psycopg2' library for connecting to the DB from Django(python)---- postgres db adapter for python
        pip install psycopg2
        
    Make changes In Models.py
        Inherit "Destination" class from models.Model
        Get the Django Model fields from google (Search for Django model fields) (https://docs.djangoproject.com/en/3.1/ref/models/fields/)
        Define all the Datatypes and sizes for the fields (name, img, price , desc)
        
    To create a table with the above Class and its fields in Postgres we have to run Migrations as below..
        Add "Tour.apps.TourConfig" in settings.py\INSTALLED_APPS 
        Install Pillow "run command "python -m pip install Pillow" (To upload Images) 
        "python manage.py makemigrations" (This will create 0001_initial.py file in migrations folder)--- detects the changes and updates the DB
        "python manage.py sqlmigrate Tour 0001" (Creates the Table in the Postgres) 
        "python manage.py migrate" (Actual migrations) 
        
     The above commands create many other tables, but our main table will be "Tour_destination"
     
     
     Modifying the Fields 
     
        ---------------ReMigration---------------
        Either change it in the Models.py (whatever you want to correct)  
            Run "python manage.py makemigrations" again (add default value at the prompt) 
            
            Run "python manage.py migrate" again
            
        OR
        ALTER the Tables using SQL quries in the DB  
        
        
Working with Admin page (http://localhost"8000/Admin)

            Run "python manage.py createsuperuser"
            username: shivayogimathd
            Email: muttu2244@gmail.com
            pwd: Sept2020*
            
            We can create Groups / Users who can login into the Websites, and give them the required permissions.
            
            To add the Destinations in the Admin page  
                use "from . models import Destination"  (Add this in admin.py)
                Register the "Destination" in the admin page by following 
                    admin.site.register(Destination) ---- (Add this also in admin.py)
            
            This will automatically register "Destinations" tab in the Admin UI page..
                We can add extra destination like (Mumbai, Bangalore, Hyderabad) using UI
        
Add and Fetch Data from Database
        To Add / delete image from the UI, we have to work with MEDIA FILES
        IN "FirstWebAppl/Settings.py" Add the following 
                MEDIA_URL = '/media/'
                MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
                
        In "FirstWebAppl/urls.py" add the following 
        
            from django.conf import settings
            from django.conf.urls.static import static 
        
            urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
             
            
        Go and add the destinations from the UI, and verify if they are coming in the DB
        
        Go to Views.py and modify as follows 
            Delete the "dests" list created earlier, we no longer need it
            Add "dests = Destination.objects.all()" 
    
        In index.html modify the images as follows 
            Change "{{ baseURL }}/{{ dest.img }}" to "{{ dest.img.url}}" 
            
        Check the Home page, and you will see the Images/Data , every thing that matches with the DB
        
Registrations
        
        Create a seperate App for Registration call it as accounts
            python manage.py startapp accounts          (This will create a seperate Accounts folder)
         
         Add urls.py in Accounts app, and add the urlPatters as follows 
                urlpatterns = [
                        path('register', views.register, name='register'),
                        ]
         
         Make the corresponding changes in FirstWebAppln/urls.py    (Main Application)
            Add "path('accounts/', include('Accounts.urls'))" to the urlpatterns
         
          
        Make changes in the index.html to remove or comment out
            'about.html', 'services.html', 'news.html'  (this is the template we have taken from Tavello colorlib, 
                so we dont need all those what is there in that, we will modify as per our need
                
             Add 'Accounts/register.html'
             
        Modify Accounts/views.py 
            Add function for register
                def register(request):
                    return render(request,'register.htnml') 
                    
        Add 'register.html' page in the templates 
            
            Get the fields from "auth_user" DB which was created automatically when we created "Tour_Destination" table
            And add them in "register.html" (FirstName, LastName, Username, pwd, confirm pwd, email etc) 
            
        Add the POST method in 'views.py' and post all the above  fields 
        Add some users through UI by clicking on Register tab
        Confirm the user is added in the DB and also in the Admin UI page
        
        Password/Email / User Verification
            In Views.py change the code to verify if the email and username already exists
            And if the pwd does not match with the confirm password
             
        
        
    
    
    


     
    