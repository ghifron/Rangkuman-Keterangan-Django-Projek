#code

“ from Django.contrib.auth.from import usercreationform
Def signup(request):
If request.POST:
From= usercreationfrom(request.POST)
From.save()
Messeger.success(request.”user berhasil dibuat!)
Retrun redirect(‘signup”)
Else:
Messages.error(request.”terjadi kesalahan!)
Retrun redirect(‘signup”)
Else:
From = usecreationfrom()
Konteks={
‘from’=from,
}
Retrun render(request,’signub.html,konteks)

#code

{% extends 'base.html' %}

{% block content %}

<div class="container">
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          Tambah User
        </div>
        <div class="card-body">
          {% for message in messages %}
            {% if message.tags == 'success' %}
              <div class="alert alert-success">{{ message }}</div>
            {% else %}
            <div class="alert alert-danger">{{ message }}</div>
            {% endif %}
          {% endfor %}
          <form action="{% url 'signup' %}" method="post">
            {% csrf_token %}

            {{ form.as_p }}

            <button class="btn btn-primary">Simpan</button>
            <a href="{% url 'users' %}" class="btn btn-danger">Kembali</a>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

{% endblock %}

#code

from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('penerbit/', penerbit, name='penerbit'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
]

"""
16. SIGN UP/TAMBAH USER

Membuat view

Langkah 1
“ from Django.contrib.auth.from import usercreationform
Def signup(request):
If request.POST:
From= usercreationfrom(request.POST)
From.save()
Messeger.success(request.”user berhasil dibuat!)
Retrun redirect(‘signup”)
Else:
Messages.error(request.”terjadi kesalahan!)
Retrun redirect(‘signup”)
Else:
From = usecreationfrom()
Konteks={
‘from’=from,
}
Retrun render(request,’signub.html,konteks)
Langkah 2 membuat file temlets
{% extends 'base.html' %}

{% block content %}

<div class="container">
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          Tambah User
        </div>
        <div class="card-body">
          {% for message in messages %}
            {% if message.tags == 'success' %}
              <div class="alert alert-success">{{ message }}</div>
            {% else %}
            <div class="alert alert-danger">{{ message }}</div>
            {% endif %}
          {% endfor %}
          <form action="{% url 'signup' %}" method="post">
            {% csrf_token %}

            {{ form.as_p }}

            <button class="btn btn-primary">Simpan</button>
            <a href="{% url 'users' %}" class="btn btn-danger">Kembali</a>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

{% endblock %}

Langkah 3
Menambah pada file url    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
 
from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('penerbit/', penerbit, name='penerbit'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
]

"""