#code

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST)
 if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

"""
14.3 CRUD:MENGUBAH DATA

mengubah data mengubah data di sini perannya sangat penting dalam aplikasi karena saat kita salah melakukan input data maka
kita harus mengubahnya atau mengoreksinya dengan menggunakan fitur update ini atau fitur ubah data ini lebih efektif dibanding
dengan saat kita hapus input ulang hapus itu lanjutnya nubah data pengubah data di sini Sebenarnya sama dengan for menambah data
bedanya song ubah data sudah terisi oleh data Apa yang akan kita ubah seperti berikut ini kita akan mengubah data buku bahasa
Indonesia ubah lalu simpan perubahan selesai

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST)
 if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)


setelah perubahan disimpan apa yang terjadi biasanya akan diri direct akan diarahkan kembali kehalaman ubah data itu sendiri
lalu muncul pesan data Brasil diperbarui kira-kira seperti itu berarti di sini kita butuh redirect bukan render 


"""