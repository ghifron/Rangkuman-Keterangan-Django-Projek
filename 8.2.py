
#code base

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PERPUSTAKAAN SEKOLAH SMK</title>

    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    
    {% include 'judul.html' %}

    {% block content %}
    {% endblock %}

    <script src="{% static 'js/jquery.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
</body>
</html>

"""
8.2 SETUP BOOTSTRAP

1. Download dulu bootstrapnya di getboostrap.com dan jquerynya di code.jquery.com
2. Kemudian copy file bootstrap.min.css ke folder static kemudian folder css. setelah itu copy
bootstrap.min.js dan jquery.js ke folder js
3. Sekarang kita memanggil file tersebut di base.html
4.Untuk pemanggilan bootstrap css diletakan di sebelum file style.css dengan perintah :

<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

5. Untuk file js di load dibawah sebelum tutup code
6. Untuk urutannya jquery dulu baru bootstrap.min.js dengan perintah :

<script src="{% static 'js/jquery.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>

"""