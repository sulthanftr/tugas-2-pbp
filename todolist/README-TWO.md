## Perbedaan _Asynchronous Programming_ dengan _Synchronous Programming_.
| _Asynchronous Programming_ | _Synchronous Programming_ |
|--|--|
| Operasi pada program _synchronous_ dilakukan satu demi satu. Hanya ketika satu operasi telah selesai dieksekusi lah operasi lain dapat dilakukan. Dengan kata lain, setiap operasi dalam program harus menunggu gilirannya untuk dieksekusi. | Operasi pada program _asynchronous_ dapat dilakukan secara pararel ketika operasi lain sedang dalam proses eksekusi. Sehingga, berbagai request dapat diproses sekaligus di saat yang bersamaan, tanpa menunggu giliran untuk eksekusi. |


## _Event-Driven Programming_
_Event-driven programming_ adalah sebuah paradigma pemrograman dimana program menunggu sebuah _event_ untuk mengeksekusi bagian dari program. Sebuah _event_ bisa dalam bentuk pemencetan suatu tombol, penerimaan pesan dari program lain, input dari perangkat I/O, dan lainnya.

Pada aplikasi Todolist, User dapat membuat _task_ baru pada halaman utama dengan mengisi _form_ yang ada dan menekan tombol _Create_. Penekanan tombol adalah suatu bentuk _event_. Ketika _event_ tersebut terjadi, program akan mengeksekusi 3 hal: Memanggil _view_ pembuatan objek Task baru, Membuat object _Task_ baru dan menyimpannya ke _database_, lalu me-_refresh_ halaman utama untuk memperbarui daftar _task_ yang ada.

## Penerapan _Asynchronous Programming_ pada AJAX
Sebuah aplikasi web dengan JavaScript dapat menerapkan AJAX (_Asynchronous JavaScript and XML_) untuk membuat aplikasi _asynchronous_ dan _event-driven_. Aplikasi web menerima _event_ dari user seperti pemencetan tombol untuk memanggil dan mengeksekusi suatu operasi secara _asynchronous_. Hal ini membuat aplikasi web menjadi lebih interaktif dan responsif ketika digunakan.

## Implementasi Tugas
- Membuat view `show_json` yang mengembalikan objek-objek `Task` milik user dalam format JSON.
- Membuat routing untuk view tersebut dengan menambahkan _path_ `todolist/json` pada `urls.py`
- Membuat script _asynchronous_ JavaScript pada `todolist.html` berbentuk fungsi `getTodolist()` yang memanggil path dari view `show_json`.
- Membuat fungsi `refreshTodolist()` yang mengiterasikan setiap task pada data yang dikembalikan `show_json`.
- Setiap iterasi, buat sebuah string HTML untuk menampilkan objek tersebut.
- Tambahkan semua string HTML dari objek ke `innerHTML` sebuah tag dengan `id='tasks'`
- Membuat view `add_task` yang menerima request POST beserta parameter `title` dan `description` sebagai attribut untuk membuat object `Task` baru.
- Membuat routing untuk view tersebut dengan menambahkan _path_ `todolist/add` pada `urls.py`
- Buat form pada halaman utama untuk membuat task baru.
- Buat script yang menerima _event_ penekanan tombol form. Ketika _event_ diterima, lakukan request POST beserta data dari form kepada _view_ `add_task`. Kemudian, panggil fungsi `refreshTodolist()`.