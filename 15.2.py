"""
15.2 MENGAKSES USERNAME DI TEMPLATE

a.	Mengakses user yang sedang aktif untuk diakses kedlam template
b.	Dimana disini ada user yang sdang aktif tapi kita tidak tau user mana yang sedang aktif dan tidak mempunyai nama 
c.	Pada bagian template di program judul.html kita tambahkan,dimana variable userini yang nantinya akan mencetak user yangsedang aktif 
			<p> {{user }} </p>
d.	Dan ketika kita keluar maka akan muncul  anonymous user secara otomatis
e.	cara menghilangkan  anonymous user
	{%if user.is-autenticated%}
	<p> {{user }} </p>
	{%endif%}

"""