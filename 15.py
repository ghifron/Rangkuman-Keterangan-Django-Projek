#code

{% extends 'base.html' %}

{% block content %}

{% if user.is_authenticated %}
  <meta http-equiv="refresh" content="0; url={% url 'buku' %}">
{% else %}
<div class="container">
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card shadow-lg">
        <div class="card-header">
          LOGIN.
        </div>
        <div class="card-body">
          <form method="post">
            {% csrf_token %}

            {{ form.as_p }}

            <button class="btn btn-primary">Masuk</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
{% endif %}

{% endblock %}

"""
15. AUTHENTICATION LOGIN AND LOGUT

Proses verifikasi / validasi identitas user yang terdaftar sebelum mengakses systemdengan ini kita dapat membatasi  usr mana
saja yang boleh menabah kata mengubah kata.

Untuk membuat usernya baru bisa menggunakan Python manage.py createsuperuser
Usename(leave blank to use purple):html
Password:
Password(again)
Createsuperuser created successfully
Langkah pertama membuat urlnya
From djanggo.control auth.views.import loginview
Kemudian untuk pola urlnya
 Path(‘masuk/”,LoginView.as_View() name=’masuk’)
Kemudian untuk menu login

{% extends 'base.html' %}

{% block content %}

{% if user.is_authenticated %}
  <meta http-equiv="refresh" content="0; url={% url 'buku' %}">
{% else %}
<div class="container">
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card shadow-lg">
        <div class="card-header">
          LOGIN.
        </div>
        <div class="card-body">
          <form method="post">
            {% csrf_token %}

            {{ form.as_p }}

            <button class="btn btn-primary">Masuk</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
{% endif %}

{% endblock %}

Saat login berhasil maka beralih ke file setting tambahkan code di paling bawa“LOGIN_REDIRECT_URL=’buku’ Ketika login berhasil akan
diarahkan ke halaman buku. Apabila menu belum login maka kita membutuhkan dekulator pada menu setting ditambahkan lagi
LOGIN_REDIRECT_URL=’masuk’ cara menggunakan LOGIN_REDIRECT_URL=’masuk’ di file view, mengimporkan file setting dengan
code”from Django.conf.import setting” dengan begitu “@login_required(login_url=setting.LOGIN_URL” Utuk logout kita membuat
viewnya dulu “From djanggo.control auth.views.import loginview,logoutView, untuk pola urlnya Path(‘keluar/”,LoginView.as_View() name=’keluar’)


"""