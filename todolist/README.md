## Fungsi `{% csrf_token %}` pada elemen `<form>`
CSRF token adalah suatu nilai unik, rahasia, dan tidak dapat ditebak yang dihasilkan secara server-side untuk setiap user. CSRF token memastikan hanya user dengan token tersebut saja yang dapat melakukan request HTTP. 

Tanpa CSRF token, seorang peretas atau siapapun dapat saja melakukan request HTTP ke website dengan parameter-parameter yang diperlukan pada form.

## Cara Membuat Elemen `<form>` Secara Manual
Untuk membuat elemen form secara manual (tanpa generator seperti `{{ form.as.table }}`, Tampilkan setiap parameter form sebagai sebuah elemen. Contohnya, untuk form login yang berisi parameter username dan password, tampilkan `{{ form.username }}` dan `{{ form.password }}`, masing-masing sebagai elemen.

## Alur Data dari Submisi User pada form HTML hingga Penyimpanan ke Database
Setelah mengisi form secara menyeluruh, mengklik tombol Submit/Post akan mengirim data form ke backend dimana fungsi view yang bersesuaian akan dipanggil. Fungsi view akan membuat objek dari Model dengan parameter-parameter yang telah diterima, kemudian menyimpannya ke *database*.

## Alur Implementasi Tugas 4

- Buat aplikasi todolist dengan: ```python manage.py startapp    todolist```, ubah direktori ke `/todolist`
- Tambahkan path `todolist` ke dalam `project_django/urls.py`: ```path('todolist/', include('todolist.urls')),```
- Buat model `Task` pada `models.py`
- Implementasikan form registrasi, login, dan logout sesuai dengan tutorial pada Lab 3
- Buat view `show_todolist` pada `views.py`
- Buat view `task_selesai` untuk mengganti value `is_finished` pada objek Task menjadi `True`.
- Buat view `undo_task` untuk mengganti value `is_finished` pada objek Task menjadi `False`.
- Buat view `hapus_task` untuk menghapus objek Task dari database.
- Buat halaman utama todolist. Buat file `todolist/templates/todolist.html`.
- Buat file `forms.py` pada folder `todolist`
- Buat sebuah class `ModelForm` bernama	`TaskForm` yang hanya memiliki field `title` dan `description`
- Buat view `create_task` pada `views.py`. Jika `request.method` bersifat `POST`, buat sebuah objek Task baru dan isi parameter sesuai dengan yang disubmit pada form. Jika tidak, buat objek `TaskForm` baru dan kembalikan sebuah render ke `create-task.html'` beserta objek tersebut.
- Buat template `create-task.html` sebagai form untuk membuat objek Task baru.
- Buat routing url pada setiap views di dalam `urls.py`
- Push ke repositori GitHub, Deploy repositori ke Heroku. Buat superuser, kemudian buat 2 user dengan masing-masing 3 objek task melalui halaman admin django.
