#code settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#code html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PERPUSTAKAAN</title>
</head>
<body>
    
    <center>
        <h1>PERPUSTAKAAN</h1>
    </center>

    <h2>Daftar Buku</h2>
</body>
</html>

#code views

from django.shortcuts import render

def buku(request):
    return render(request, 'buku.html')

"""
7.1 TEMPLATES

1. buka settings.py di perpus dan di bagian TEMPLATES kemudia DIRS
isi dengan 'templates' dimana file html kita disimpan di folder template

2. kemudian buat folder templatesnya di satu level dengan file perpus dan perpustakaan
3. setelah itu buat file html di template dan buat html sederhana
4. kemudian di file views.py hapus saja from django.http import HttpResponse dan
ganti dan tambahkan code return render(request, 'buku.html') di method buku



"""