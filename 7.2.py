#code views substitute Variable

from django.shortcuts import render

def buku(request):
    judul = "Belajar Django"

    konteks = {
        'title': judul
    }
    return render(request, 'buku.html', konteks)

#code buku

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

    {{ title }} <br>

    {{ penulis }}
</body>
</html>

#code views filter

from turtle import penup
from django.shortcuts import render

def buku(request):
    judul = "Belajar Django"
    penulis = "Zul Hilmi"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)

#code buku 2

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

    {{ title | upper }} <br>
    {{ penulis }}

</body>
</html>

#code tags

from turtle import penup
from django.shortcuts import render

def buku(request):
    judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
    penulis = "Zul Hilmi"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)

#code buku 3

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

    {% for judul in title %}
        <li>{{ judul }}</li>
    {% endfor %}
    {{ penulis }}

</body>
</html>

"""
7.2 TEMPLATE LANG

1. Substitute Variable
2. Filter
3. Tag

1. Substitute Variable

-Di method buku buat variabel judul dengan isi belajar django
-kemudian membuat konteks yang berbentuk dictionary yang untuk mengumpulkan data-data variabel
-untuk keynya dengan title dan valuenya judul
-di render tambahkan konteks

-dan di file buku.html panggil key title dengan kurung kurawal sama-sama dua kali buka dan tutup kurung

2. filter

disini mengubah kalimat menjadi huruf besar/kecil semua

- dengan tanda garis vertikal | dan diikuti perintah upper

3. tags

control flow

-membuat dulu list di variabel judul dengan isi

judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]

-untuk pemanggilan di file htmlnya menggunakan perintah

{% for judul in title %}
        <li>{{ judul }}</li>
    {% endfor %}






"""