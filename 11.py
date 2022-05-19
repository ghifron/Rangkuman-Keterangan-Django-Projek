"""

11. DJANGO ADMIN

django admin adalah salah satu fitur yang powerful yang ada pada jenggot dikatakan powerful karena bisa melakukan grup sederhana
untuk mengolah data pada model yang kita buat Hai ini adalah tampilan Jinggo buku penerbitan lain itu merupakan model-model model
nanti yang kita buat akan didaftarkan ke dalam Jinggo admin disini kita bisa mengolahnya bisa menambahkan data buku data kelompok
mengubah dan menghapus data biasanya.

Mari kita praktekkan sebenarnya saat kita membuat Project ada url yang sudah dibuatkan oleh jenggotnya yaitu admin untuk mengakses
django kalau kita akses langsung flash.bin cap jago admin login

Mari kita buat akunnya buka 

terminal python manage.py createsuperuser username(leave blank to use ‘purpele’) admin 

Email address : admine@sekolah.sch.id
Password (again)
Python manager.py runserver
jika sudah membuat akun hai lalu kita coba login 

 selanjutnya kita menampilkan model yang kita buat ke dalam Jinggo admin buka Project dengan text editor lalu mengedit file admin.py 
from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)

model-model yang kita buat sudah masuk sudah terdaftar perpustakaan adalah nama esnya buku kelompok adalah model powerful nya disini
Di sini ada tombol X kalau kita klik kita lihat ada sebuah form untuk menambahkan data ke dalam databook ke dalam model buku kita hanya membuat kelas modal saja kelas buku itu didaftarkan ke dalamnya


"""