## Perbedaan antara JSON, XML, dan HTML

 - **JSON** (JavaScript Object Notation) adalah sebuah bahasa notasi objek yang berdasarkan Javascript. JSON berfokus dalam merepresentasikan data dalam bentuk objek. JSON mendukung array dan comments tetapi tidak mendukung namespaces. JSON hanya mendukung encoding UTF-8
 - **HTML** (Hyper Text Markup Language) adalah bahasa markup yang dikembangkan dari SGML (Standard Generalized Markup Language) yang berfokus dalam kenyamanan penggunaan. HTML digunakan secara luas untuk tampilan halaman website. HTML mendukung comments, berbagai encoding, dan dapat menampilkan data dari framework.
 - **XML** (Extensible Markup Language)  dikembangkan setelah HTML untuk melengkapi kembali fitur-fitur dari SGML yang hilang. XML mendukung namespaces dan commens, tetapi tidak mendukung array dan cenderung lebih sulit untuk dibaca dibandingkan dengan JSON atau HTML. Meskipun demikian, XML lebih aman dibandingkan JSON dan mendukung lebih banyak encoding daripada HTML.

## Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Internet pada awalnya hanyalah suatu tempat untuk membaca suatu informasi yang di tampilkan pada sebuah halaman static. Tapi seiring berkembangnya kecepatan internet, pembaruan server, dan peningkatan kemampuan para developer, Internet berevolusi dari informasi static menjadi aplikasi web yang interaktif dan dapat menampilkan, mengirim, mengubah, dan menghapus konten/data secara dinamis. Untuk dapat melakukan ini, diperlukan sebuah protokol yang dapat berkomunikasi antar berbagai perangkat untuk mengirim data (data delivery) dari web server ke halaman aplikasi dan sebaliknya dengan instan. HTTP (HyperText Transfer Protocol) memenuhi kebutuhan tersebut. HTTPS, dengan "S" berarti secured, mengenkripsi data yang ditransfer demi keamanan dan pencegahan campur tangan pihak ketiga.

## Mengimplementasikan aplikasi _My Watchlist_.
1. Buat aplikasi mywatchlist dengan `python manage.py startapp mywatchlist`
2. Buat config aplikasi yaitu MywatchlistConfig dalam `apps.py`
3. Buat model MyWatchList dalam `models.py` dan isi attributes dengan field yang sesuai.
4. Daftarkan aplikasi dalam `admin.py` serta dalam INSTALLED_APPS pada file `project_django/settings.py`
5. Lakukan migrasi dengan `python manage.py makemigrations` lalu `python manage.py migrate`
6. Jalankan server dengan `python manage.py runserver`, akses halaman admin dan cek jika table aplikasi kita telah muncul.
7. Buat folder templates di dalam `mywatchlist` dan tambahkan file mywatchlist.html
8. Dalam `views.py` buat sebuah fungsi view untuk menampilkan halaman HTML. Buat sebuah parameter yang berisi query seluruh objek MyWatchlist dengan `MyWatchList.objects.all()`
9. Tampilkan pesan yang sesuai dengan banyak/sedikit menonton dengan menggunakan if statement terhadap jumlah film yang sudah ditonton dan belum (gunakan `MyWatchList.objects.filter(watched=True).count()` dan `watched=False` untk yang belum ditonton)
10. Kembalikan render ke mywatchlist.html dengan `return render(request, "mywatchlist.html", context)`
11. Dalam `templates/mywatchlist.html`, buat for loop yang mengiterasi objek-objek MyWatchList dari parameter view sebelumnya.
12. Tampilkan pula pesan banyak/sedikit menonton yang sudah diberikan sebelumnya
13. Pada `mywatchlist/urls.py`, daftarkan url yang menampilkan view yang baru dibuat. Lalu pada `projek_django/urls.py`, daftarkan url tersebut.
14. Pada `views.py`, buat 2 fungsi view: view yang menampilkan xml dan view yang menampilkan json.
15. Tambahkan routing url untuk kedua views tersebut di dalam `mywatchlist/urls.py`.
16. Buat migrasi dengan `python manage.py makemigrations` lalu `python manage.py migrate`
17. Buat folder dan file `fixtures/initial_mywatchlist_data.json` lalu buat 10 data untuk objek `MyWatchList`. kemudian load data tersebut dengan `python manage.py loaddata initial_mywatchlist_data.json`
18. Dalam `Procfile` tambahkan command `python manage.py loaddata */fixtures/*.json` sebagai command yang dijalankan pada deployment heroku
19. Commit dan push perubahan dan ke repositori github.
20. Jalankan kembali workflow yang gagal pada repositori github.
21. Akses halaman yang ter-deploy pada link aplikasi heroku. 

### HTML Response
![HTML response](https://res.cloudinary.com/dbev4mnac/image/upload/v1663808533/Screenshot_2022-09-21_221320_bqxwuj.png)

### JSON Response
![JSON Response](https://res.cloudinary.com/dbev4mnac/image/upload/v1663808533/Screenshot_2022-09-21_221506_dmxbtf.png)

### XML Response
![XML Response](https://res.cloudinary.com/dbev4mnac/image/upload/v1663808533/Screenshot_2022-09-21_221454_h8iiki.png)

## Testing
Jalankan `python manage.py test`
