## Perbedaan dari Inline, Internal, dan External CSS
| | Inline | Internal | External |
|-|--|--|--|
|Perbedaan|Diletakkan pada attribut `<style>` dalam tag| Diletakkan di dalam tag `<head>` pada halaman|Diletakkan pada sebuah file .css|
|Kelebihan|Perbaikan cepat, ukuran HTTP request kecil, berguna ketika  ingin melihat perubahan|HTML dan CSS tergabung dalam 1 file, Dapat memanfaatkan ID dan Class|HTML terpisahkan dari CSS sehingga lebih terorganisir, kecepatan loading menjadi cepat, file .css dapat digunakan pada berbagai halaman
|Kekurangan|Harus diletakkan pada setiap tag| CSS hanya dapat merubah 1 halaman, memperlambat akses website|Perlu menunggu file .css terpanggil agar styles yang diberikan pada HTML tampil

## Penjelasan beberapa tag HTML
- `<div>`: Mendefinisikan sebuah divisi atau bagian dari sebuah dokumen HTML
- `<p>`: Merepresentasikan paragraf
- `<h1>` hingga `<h6>`: Merepresentasikan Header halaman, dengan h1 ukuran terbesar hingga h6 ukuran terkecil
- `<a>`: Mendefinisikan hyperlink
- `<span>`:  Sebuah tag generik yang tidak membentuk baris baru sehingga mudah untuk melakukan perubahan di dalam baris
- `<body>`:  Mendefinisikan body dari sebuah dokumen HTML, isi dari body HTML adalah seluruh konten dari dokumen tersebut
- `<head>`:  Berisikan metadata dari suatu dokumen HTML
- `<button>`:  Mendefinisikan sebuah tombol
- `<input>`:  Mendefinisikan sebuah input yang dapat dimasukkan melalui tampilan halaman HTML
- `<li>`:  Mendefinisikan sebuah list
- `<ol>`: Mendefinisikan sebuah elemen terurut dari suati list
- `<ul>`: Mendefinisikan sebuah elemen tak terurut dari suatu list
- `<tb>`: Mendefinisikan sebuah tabel
- `<th>`: Mendefinisikan sebuah sel header pada suatu tabel
- `<tr>`: Mendefinisikan sebuah sel baris pada suatu tabel
- `<main>`: Mendefinisikan konten utama dari suatu dokumen HTML
- `<link>`: Mendefinisikan suatu hubungan antara dokumen HTML dengan suatu sumber eksternal
- `<form>`: Mendefinisikan sebuah form berisi input untuk user 
- `<label>`: Mendefinisikan label dari beberapa elemen pada HTML

## Selector CSS
- Element Selector (with leading # or .): Menerapkan CSS pada semua element dengan tag yang dipilih
- Class Selector (with leading .): Menerapkan CSS pada setiap tag dengan class yang dipilih
- ID Selector (with leading #): Menerapkan CSS pada setiap tag dengan id yang dipilih

## Implementasi Tugas
- Install framework CSS Bootstrap pada `base.html`
- Buat folder `static` pada aplikasi `todolist`
- Terapkan style Bootstrap pada class dari masing-masing element pada dokumen HTML `login.html`, `register.html`, `create-task.html`, dan `todolist.html`
- Tambahkan CSS eksternal untuk setiap dokumen HTML pada folder static. `forms.css` untuk halaman login, register, dan create task. `todolist.css` untuk halaman todolist.