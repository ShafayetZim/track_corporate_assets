# corporate_asset_track_coding_challenge

<b>Project Installation in Django Python:</b>

1. Download and install python 

2. Create Virtual Environment<br />
linux & mac os: python3 -m venv environment_name<br />
Windows: python -m venv environment_name
  
3. Activate Environment<br />
  #Linux & mac os<br />
  ->source environment_name/bin/activate<br />
  #Windows<br />
  ->environment_name\Scripts\activate
  
4. Install Django, rest & other requirements <br />
 ->pip install django<br />
 ->pip install djangorestframework<br />
 ->pip install psycopg2-binary<br />
 ->pip install drf-yasg<br />
  
5. Go to project directory & execute:<br />
-> Migration: python manage.py makemigrations<br />
-> Migrate: python manage.py migrate

6. Create superuser <br />
->python manage.py createsuperuser
	enter username, Email, password
	enter your password again

7. Run server: <br />
-> python manage.py runserver<br />

That's it! <br />
Remember to run the server using 'python manage.py runserver' and access the application <br>