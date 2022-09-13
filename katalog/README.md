## Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

[Link website heroku](https://tugas2pbp-katalog.herokuapp.com/katalog/)

![Bagan](https://res.cloudinary.com/dbev4mnac/image/upload/v1663050754/S__28745731_twqhhy.jpg)

**Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?:**
- Untuk menjaga konsistensi seluruh package beserta versi nya
- Agar package terorganisir untuk masing2 project dan tidak tercampur-campur
- Memisahkan environment python komputer kita dengan environment python project aplikasi

**Cara implementasi tahap 1 sampai 4:**
<br />
 Tahap 1:
 1. Buat superuser, migrate project django, dan tes project dengan runserver
 2. Register app katalog dalam katalog/admin.py
 3. Tes table katalog dengan load data dari initial_catalog_data.json
 4. Membuat fungsi show_catalog yang menerima request. Di dalam fungsi, buat parameter data_katalog yang menerima semua objek
 dengan model CatalogItem (menggunakan Catalog.objects.all())
 5. Membuat parameter context yang berisi data-data dari parameter data_katalog
 6. Mengembalikan HTTP Response dengan HTML yang berisi data pada context (menggunakan return  render(request, "katalog.html", context))

Tahap 2:
1. Membuat url yang menampilkan view show_catalog dalam katalog/urls.py
2. Memasukkan url tersebut ke dalam daftar url project kita di project_django/urls.py

Tahap 3:
1. Membuat for loop yang mengiterasi objek-objek CatalogItem
2. Di dalam setiap for loop, tampilkan detail objek tersebut (nama, stock, harga, rating, description, url)

Tahap 4:
1. Commit, dan push pekerjaan ke repositori github
2. Buat aplikasi baru di website Heroku untuk project ini
3. Tambahkan dua secrets pada repositori github project ini: HEROKU_APP_NAME dan HEROKU_API_KEY
4. Di repositori, ke Actions -> Workflow runs dan jalankan ulang workflows yang gagal. Tunggu hingga berhasil agar website ter-deploy dan dapat dibuka

## Demonstrasi Unit Test model CatalogItem
Jalankan `python manage.py test`
