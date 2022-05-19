#code

{% extends 'base.html' %}

{% block content %}

<div class="container">
  <div class="row">
    <div class="col-md-4">
      <h3>Tambah Buku</h3>
      
      {% if pesan %}
        <div class="alert alert-success">{{ pesan }}</div>
      {% endif %}
      
      <form action="{% url 'tambah_buku' %}" method="post" enctype="multipart/form-data">
        {% csrf_token %}

        {{ form.as_p }}
      
        <button class="btn btn-primary">Tambah Buku</button>
        <a href="{% url 'buku' %}" class="btn btn-danger">Kembali</a>
      </form>
    </div>
  </div>
</div>

"""
13.2 FROM:WIDGETS

menambahkan atribut menggunakan Gadget pada input yang sudah kita buat di episode sebelumnya Sekarang kita akan mencoba menambahkan
atribut kelas dan memanggil class but saat Hai dan lihat apa yang terjadi terhadap form input ini baik kita kembali ke teks editor
masih di file forms.py disini pertama-tama kita impor kanguru foxnya from jenggot impor pom-pom di bagian Meta kita tambahkan widget
judul film apa yang akan kita ubah yang akan kita sisipkan atribut ke dalam input teks nya kedalam form input di sini kita coba 
judul dulu form Static text input atau siput ini adalah tipe yaitu input type text Karena judul adalah percaya sama dengan inputtype
tekstur maka disini inputtype teks kalau misalkan tipenya text area nanti kita tulis text area ataupun sale kita tulis baru-baru di
sini kita tulis atribut dan value-nya akibatnya adalah kelas Hai input teks ya tambahkan atribut kelas value-nya VOC kontrol kita
Panggil kelas kontrol yang ada pada bootstrap nanti kita lihat apa yang terjadi 

cara menggunakan app busrat ya Bagaimana cara menyusun struktur plus bootloop seperti ini kontainer bawa kemudian kolom playlistnya
ada di channel ini ya nanti silahkan lihat ada di deskripsi lalu formnya yang sudah tadi yang tadi kita kap kita masukkan kesini ke
dalam kolam D4 lalu kita tambahkan

{% extends 'base.html' %}

{% block content %}

<div class="container">
  <div class="row">
    <div class="col-md-4">
      <h3>Tambah Buku</h3>
      
      {% if pesan %}
        <div class="alert alert-success">{{ pesan }}</div>
      {% endif %}
      
      <form action="{% url 'tambah_buku' %}" method="post" enctype="multipart/form-data">
        {% csrf_token %}

        {{ form.as_p }}
      
        <button class="btn btn-primary">Tambah Buku</button>
        <a href="{% url 'buku' %}" class="btn btn-danger">Kembali</a>
      </form>
    </div>
  </div>
</div>

"""