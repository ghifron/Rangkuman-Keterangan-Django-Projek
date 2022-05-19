#code settings

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#code style

body {
    background-color: bisque;
}

#code base

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PERPUSTAKAAN SEKOLAH SMK</title>

    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    
    {% include 'judul.html' %}

    {% block content %}
    {% endblock %}

</body>
</html>

"""
8. STATIC FILE

Kumpulan file CSS, JS, dan Gambar

1. Masuk ke menu settings dan di bagian STATIC_URL buat baris baru dan masukan code :

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

note : Untuk code dari STATICFILES_DIRS setiap versi django berbeda. Untuk melihat codenya ada di syntax yang di koment
contohnya : # https://docs.djangoproject.com/en/4.0/howto/static-files/

2. Kemudian buat folder dengan nama static
3. Di dalam folder static buat 3 folder dengan nama folder : css, js, dan images
4. Setelah di folder css, buat file CSS dengan nama style.css kemudian isi dengan code berikut :

body {
    background-color: bisque;
}

5. Dan yang terakhir di file base.html isi dengan code :

{% load static %} : diawal baris dan
<link rel="stylesheet" href="{% static 'css/style.css' %}"> : sebagai penghubung file cssnya


"""