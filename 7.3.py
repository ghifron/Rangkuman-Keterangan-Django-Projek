#code penerbit

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

#code base

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PERPUSTAKAAN SEKOLAH</title>
</head>
<body>
    
    {% block content %}
    {% endblock %}

</body>
</html>

#code buku

{% extends 'base.html' %}

{% block content %}
    <center>
        <h1>PERPUSTAKAAN</h1>
    </center>

    <h2>Daftar Buku</h2>

    {% for judul in title %}
        <li>{{ judul }}</li>
    {% endfor %}
    {{ penulis }}
    
{% endblock %}

#code penerbit 2

{% extends 'base.html' %}

{% block content %}
    <center>
        <h1>PERPUSTAKAAN</h1>
    </center>

    <h2>Daftar Penerbit</h2>

{% endblock %}

#code judul

<center>
    <h1>PERPUSTAKAAN</h1>
</center>

#code base 2

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PERPUSTAKAAN SEKOLAH SMK</title>
</head>
<body>
    
    {% include 'judul.html' %}

    {% block content %}
    {% endblock %}

</body>
</html>

# code penerbit 3

{% extends 'base.html' %}

{% block content %}

    <h2>Daftar Penerbit</h2>

{% endblock %}

"""
7.3 TEMPLATE EXTENDING

1. membuat terlebih dahulu file penerbit.html dan base.html di folder templates
2. di bagian body isi membuat tags dengan perintah :

{% block content %}
{% endblock %}

bagian ini dimana nanti akan diisi oleh konten konten
dari template apps.
jadi templates yang ada di apps nanti akan masuk di extend

3. kemudian buat folder templates di folder perpustakaan dan pindahkan
file penerbit.html dan buku.html ke folder templates yang ada di perpustakaan
4. di file buku.html kita tidak perlu mmenulis struktur html lengkap, kita hanya membuat bagian bodynya saja, karena di bagian bodynya ini yang masuk di bagian block content didalam base.html begitu pun juga dengan penerbit dengan perintah :

{% extends 'base.html' %}

{% block content %}

{% endblock %}

5. kemudian kita pisahkan menjadi file tersendiri, dan kita pisahkan di folder templates utama dengan membuat file judul.html di folder templates utama.

dengan code htmlnya :

<center>
    <h1>PERPUSTAKAAN</h1>
</center>

6. di bagian base.html dengan code :

{% include 'judul.html' %}

7.
"""