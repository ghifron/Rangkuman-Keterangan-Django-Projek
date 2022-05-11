#code urls
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def buku(request):
    return HttpResponse('Halaman Buku')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
]

#code views
from django.shortcuts import render
from django.http import HttpResponse

def buku(request):
    return HttpResponse('Halaman Buku')

#code urls 2

from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
]

"""
7. MEMBUAT VIEWS

1. yang pertama di file urls.py di perpus, kita memindahkan code dari barisan httpRespone sampai method buku ke file views.py
di app perpustakaan kemudian paste
2. setelah itu di file urls.py tambahkan perintah :

from perpustakaan.views import buku

3. setelah itu jalankan
"""