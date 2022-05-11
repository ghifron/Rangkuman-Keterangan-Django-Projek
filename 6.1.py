#code settings

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perpustakaan',
]

"""
6.1 MEMBUAT APPS

1. disini kita membuat appnya dulu di CMD didalam folder perpus
dengan perintah :

django-admin startapp perpustakaan

2. setelah itu kita masuk ke PROJEK perpus dan pilih menu settings.py
3. kemudian di method "INSTALLED_APPS" kita tambahkan nama app yang dibuat tadi yaitu dengan nama 'perpustakaan' seperti code diatas
4. di folder perpustakaan ada file

__init__.py
admin.py : untuk meregistrasikan model yang kita buat untuk ditampilkan ke django admin
apps.py : file untuk membantu user untuk membantu menkonfigurasikan apss
models.py : isinya kelas-kelas untuk memodelkan tabel ke database
test.py : untuk testing
views.py : file yang isinya fungsi-fungsi untuk melakukan proses httpresnponse, request dari client
"""