#code urls

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def buku(request):
    return HttpResponse('Halaman Buku')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
]

"""
5. Basic Routing


Disini kita membuat pola URL(Halaman) baru dengan basic dasar

1. buka file urls.py
2. kemudian di "urlpatterns" bagian path, kita tambahin path buat halaman/URL baru
3. setelah itu arti dari "admin.site.urls" adalah sebuah view yang menampilkan text halaman buku
4. dan yang terakhir membuat method buku yang membuat text output "Halaman Buku" (untuk SC lebih lengkapnya ada diatas)

"""