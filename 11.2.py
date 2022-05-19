"""

11.2 DJANGO ADMIN:MODEL ADMIN

kita akan melakukan kustomisasi sederhana Hai terhadap tampilan data buku kira-kira seperti ini I feel feel apa saja yang
akan kita tampilkan sebagai informasi seperti judul penerbit penulis dan lain-lain mengungkit akan menampilkan kotak pencarian
dan juga filter-filter kelompok buku adaptif normatif atau produktif baik buka test drivernya kita masih mengedit file admin 

from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
  list_display = ['judul', 'penulis', 'kelompok_id', 'jumlah']
  search_fields = ['judul', 'penulis', 'penerbit']
  list_filter = ('kelompok_id',)
  list_per_page = 4

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)

sekarang tampilannya lebih informatif judul buku penulis ini siapa penerbit dan jumlahnya ada berapa ini sudah terbagi menjadi dua halaman lakukan pencarian web berdasarkan judul pemograman web  jenggo Coba kita akan lakukan filter buku produktif saja buku normatif saja adaptif semua kelompok ID Apa yang akan terjadi berhubungan dengan metode STR. metode STR itu akan mengembalikan Pada representasi model adalah nama kelompok maka ini akan tampil saat kita memanggil film yang maka dia akan mengembalikan Nama judulnya apa Nama kelompoknya .

"""