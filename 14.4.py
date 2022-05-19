#code

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    return redirect('buku')

"""
14.4. CRUD:HAPUS DATA

ini kita akan  membuat fitur hapus data dan kita akan menambahkan kolom action atau aksi ya d e ah data buku nanti setiap record
itu bisa kita hapus bisa kan kita akan menghapus bpo ada tombolnya hapus hilang datanya oke nah sebenarnya hapus data ini
sangat-sangat simple ya enggak ga 2kali sangat ya simple aja simpel aja pertama-tama kita buat kolom dulu link untuk membuat
actionnya kita ke  template buku.html di bagian header tambahkan setelah kelompok  <th>ACTION</th> lalu dibawah kita tambahkan 
<a href="{% url 'hapus_buku' buku.id %}" class="btn btn-danger">Hapus</a> selanjutnya membuat actionnya buat viewnya proses hapusnya

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    return redirect('buku')

terakhir membuat urls.py 

 path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
 data berhasil dihapus secara 10 tangkap misalnya di bagian di bawah judul buku di sini ya hal ini sama dengan ubah buku ya
 dengan ubah buku mana itu babuku for message dicopy saja sama Hai Pasti sangat Hai medives Coba kita hapus buku PPL apakah
 naik akan menghapus pemodelan perangkat lunak ya data berhasil dihapus secara hai hapus baik Nah itu bagian hapus data simple
 simple banget ya maunya Jadi kita cuma seperti ini jadi yang agak pusingnya agak ribet nya di bagian hapus data ini mungkin di
 bagian ah membuat modal ya itu ya karena dirinya cuma sedikit


"""