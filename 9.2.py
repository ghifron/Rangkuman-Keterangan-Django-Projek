
#code setting

DATABASE = {
	‘default’ : {
		‘ENGINE’ : ‘django.db.backends.mysql’,
		‘NAME’ : ‘perpus’
		‘USER’ : ‘root’
		‘PASWORD’ : ‘ranger46’ ,
		‘HOST’ : ‘localhost’
		‘PORT’ : ‘3306’,
}

"""

9.2 SETUP DATABASE: MySQL

1.	Konfigurasi database pada settings.py.
2.	Install mysqlclient.
3.	Lakukan migrasi untuk menerapkan model ke database

pip install mysqlclient
python manage.py makemigrations
python manage.py migrate

"""