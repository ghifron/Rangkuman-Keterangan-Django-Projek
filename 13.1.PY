"""
13.1 FROM:MODELFROM

pembuatan aplikasi tidak terlepas dari yang namanya file baik itu form untuk menambah data ataupun mengubah data nah form inilah
yang biasa ditulis dengan html input type text input type number input tipe Day Dan lain-lain inputtype inilah yang harus
disesuaikan dengan tipe data di tabel database membuat form dengan menggunakan model volt djengo kita tidak perlu repot-repot untuk
membuat form dengan html karena kita bisa membuatnya dari model yang kita buat ini opsional membuat form saja tidak sampai ke
menyimpan data ke database 

from django.forms import ModelForm
from perpustakaan.models import Buku

class FormBuku(ModelForm):
  class Meta:
    model = Buku
    fields = '__all__'


fields ini kita akan menggunakan semua file yang ada didalam model buku yang akan ditampilkan ke form input. kita buat views.py jangan lupa impor kan from perpustakaan forms import from

tipe input ini Hai yang sesuai dengan tipe data pada tabel di database teks number integer dan lain-lain Nah di sini juga kita bisa kita buka Firefox disini jadi kita bisa memfilter memperbolehkan view mana saja yang hanya ditampilkan yang boleh ditampilkan 

"""