#code

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
17. UPLOAD FILE

membahas upload file pada django sebagai contoh kita akan melakukan upload cover buku kita akan menambahkan file baru ya pada
model buku yang bernama cover sehingga default tambah Bogor nanti akan muncul form input baru yaitu cover seperti ini ataupun
di form ubah buku gitu  dan didata Bukit akan menambahkan kolom baru yaitu cover ini sebagai informasi Buku Bagaimana caranya
pertama kita buka file setting kita lakukan pengaturan dulu di baris paling bawah

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


“MEDIA_URL = '/media/' ”untuk mengakses url file gambar kita file cover, “MEDIA_ROOT = os.path.join(BASE_DIR, 'media'  “ dimana file
gambar tersebut akan disimpan akan diupload di folder di media agar di media url bisa diakses di template kita tambahkan konteks
prosesor media di dalam tempel di sini kita duplikat di baris request lalu kita ubah request nya menjadi media save 
   'django.template.context_processors.media',
Langkah kedua kita tambahkan file baru yaitu cover di dalam model di sini kita membutuhkan bidang model yang bernama image file
image Ini mesti kita install dulu karena itu berupa PX yang bernama pillor kembali ke model cover model image file
“cover = models.ImageField(upload_to='cover/', null=True) menambahkan agar file yang di upload file gambar yang diupload nanti
akan masuk ke dalam folder media folder cover baru file gambarnya kita tambahkan “null=True” karena ini adalah file baru yang
ditambahkan kedalam model yang sudah dibuat, tanggal = models.DateTimeField(auto_now_add=True, null=True)

langkah selanjutnya kita ke views    form = FormBuku(request.POST, request.FILES)
files saat kita mengirim data mencubit data dengan memompa mengirim file-file tersebut akan ditempatkan di request file ini maka
itu ini juga berlaku untuk view ubah buku kita copy     form = FormBuku(request.POST, request.FILES, instance=buku)
selanjutnya kita ke template tambah buku di sini penting tambahkan atribut enctype="multipart/form-data">atribut ini wajib
dibubuhkan berlaku untuk form ubah buku

"""