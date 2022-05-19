#code

<div class="alert alert-success">{{ message }}</div>
       <div class=”row”>
        <div class”col-md-12>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>COVER</th>
            <th>JUDUL</th>
            <th>PENULIS</th>
            <th>PENERBIT</th>
            <th>JUMLAH</th>
            <th>KELOMPOK</th>
          
          </tr>
        </thead>
        <tbody>
          {% for buku in books %}
          <tr>
            <td>

"""
14.2 CRUD:MENAMPILKAN DATA

mengubah tampilan daftar bukunya ke dalam bentuk tabel ya agar sedikit lebih rapi kita hanya menampilkan judul saja jadi baik
kita ke file buku.html kita ubah dulu tampilannya di bagian body kita lakukan looking untuk mengambil data dari model buku lalu
kita tampilkan datanya disini baris ke-1 kolom ke-1 buku titik judul terus penulis,penerbit, jumlah dan kelompok Underscore ID 
tambahkan table border 

<div class="alert alert-success">{{ message }}</div>
       <div class=”row”>
        <div class”col-md-12>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>COVER</th>
            <th>JUDUL</th>
            <th>PENULIS</th>
            <th>PENERBIT</th>
            <th>JUMLAH</th>
            <th>KELOMPOK</th>
          
          </tr>
        </thead>
        <tbody>
          {% for buku in books %}
          <tr>
            <td>

tabel kelompok yaitu id buku kelompok ID itu ya seperti itu yang hai eh ini bukan ya saya lupa lagi where i Hai kelompok
Hai nama = produktif ya pokoknya gitulah panjang ya kalau kita menggunakan kuota SQL kita tidak perlu lagi kita hanya menggunakan
query

terakhir limit data limit data itu Hai seperti ini ya kalau bsql limit misalkan hanya 3data saja yang ditampilkan di dalam periset
kita tambahkan di bagian akhir itu bracket titik dua tiga ini adalah limit  kalau kita refresh Hai hanya menampilkan data sebanyak
tiga dua sebanyak dua setempat produktif 4

"""