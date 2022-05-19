"""
18. EXPORT FILE

a.	Ekport file menggunakan pekage dimana terlebih dahulu kita akan menginstal pekage terlebih dahulu di terminal dengan nama
package Django - import – eksport  
b.	Pada folder perpustakaan kita buat program baru dengan nama resource.py
From import – eksport  import resource
From perpustakaan.model import Buku
Class meta :
Model = buku 
c.	Kemudian kita buat view untuk ekspport data 
	From perpustakaan.resource import  Bukuresource
d.	Ekspor data buku kedalam export_xls
	Def  exsport_xls (request) :
	Buku = Bukuresource()
	Dataset = buku.exsport()
	Resfond = httpresponse (dataset.xls,content_type=’ ‘)
e.	Buat URL 
	Path (‘export/xls/’ , exsport_xls, name=’ exsport_xls’),
f.	Memperbolehkan data buku yang dimunculkan 
	Fields = [ ‘judul ‘ , ‘ tangga; ‘, ‘ kelompok _id_nama’,’penerbit’,’jumlah’]	
			<href>= {%url  ‘exsport_xls ‘ %} class =“ btn btn  - success ”> exsport_xls </href>

"""