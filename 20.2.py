"""
20.2 DEPLOYMENT

MempersiapkAn  kebUtuhan apa saja uNtuk mendiploy  aplikasi kita ke server 
Dimana disini kita akan mendeploy aplikash perpustakaan kita ke server
Untuk proses yang pertama kita buat dulu aplikash kita di computer server lalu di upload ke github kemundian nntinya ny akan
ditarik oleh computer server  untuk di defploy disana.

a.	Kita remote dulu user dengan degan cara masuk menggunaakan id dan password user yang dibuat contohnya
	Ssh zulx@192.168.100.8
b.	Ada 4 bagian dalam melakukan proses defloyment 
Update install python 3
Intall app perpustakaan
Membuat service gunicarn
Configurasi nginx
c.	Langkah pertama yaitu kita mengaupdate  engan perintah 
	Sudo apt - get update
d.	Kemudian intall python 3 di server
	Sudo apt – get install python3-pip python3-dev nginx
e.	Upgrade pip dan install venv
	Sudo –H pip3 install --upgrade pip
	Sudo –H pip3 install virtualenv
d.	Install aplikasi github yang di clone dari github,untuk penyimpanan directori akan di
	simpan di /home/zulx atau bisa juga diganti dengan nama user masing”
		git clone https”/github.com /writerlab/perpus
e.	Untuk melihat working directori 
		Cd perpus
		Pwd
		/home/zulx/perpus
f.	Sekarang kita buat virtualenv dengan nama forder env dan mengaktifkan env
	Virtualenv . env
	Source .env/bin/active
g.	Install pakage untuk kebutuhan projek
	Pip install django ==2.2.12 pillow django – import – eksport  gunicorn
h.	Konfogurasi host 
	Nano perpus/ settings.py
i.	Di allowed_host kita isikan id server kita 
	192.168.100.8
j.	lalu buat static root
	statatic root = os.path.join  (BASE_DIR, ‘static/’)
k.	menyimpan konfigurasi dan keluar
		control o kemudian enter
		control x
l.	kemudian kumpulkan semua konten static kelokasi dir yang sudah di config
		python manage.py collecstatic
m.	buat axception untuk port 8000
		sudo ufw allow 8000
n.	tes gunicarn untuk melayani projek kita
		python manage.py runserver 0.0.0.0:8000
		gunicorn –bind 0.0.0.0:8000 perpus.wsgi
o.	keluar dari env deactivate
p.	buat file service gunicorn 
		sudo nano /etc/system/system/gunicorn.service
q.	start dan enable gunicorn
	sudo system start gunicorn
	sudo system enable gunicorn


"""