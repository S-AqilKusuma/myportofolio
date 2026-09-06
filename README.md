Nama : Sayyid Aqil Kusuma

NPM : 2506596331

Kelas : PBP C


### Tugas 1

1. Saya menggunakan elemen \<section>, \<details>, \<summary>, \<p>, dan \<img> dalam membuat bagian baru untuk skill. Saya menggunakan kelima elemen ini untuk membantu saya dalam mengindentifikasi satu bagian dari bagian lainnya seperti \<section class="hero-skills"> dengan bagian lain. Saya juga menggunakan \<details> dan \<summary> untuk menghemat ruang layar agar lebih rapih. Saya memisah \<p> dari \<details> agar saya bisa menentukan penempatan dari deskripsi skill secara independen terlepas dari properti milik \<details>. Selain itu, saya juga dapat mengatur penempatannya jika saya perlu menambahkan elemen lain ke dalam \<details>. \<img> digunakan untuk memberikan logo skill pada setiap skill (kecuali skill yang tidak memiliki logo seperti OOP). Dengan menggunakan bantuan \<a>, saya bisa menempelkan link web sumber dari gambar yang saya letakkan di dalam \<img>.

2. Ketika saya ingin menambahkan \<section> untuk skill, saya sempat berpikir bahwa skill-skill tersebut bisa saja memakan banyak sekali ruang jika skill yang saya punya sudah sangat banyak, apalagi ditambah deskripsi dari masing-masing skill. Ketika memikirkan hal itu, saya teringat tentang bagian dari web yang bisa di-scroll secara independen terlepas dari keseluruhan halaman web seperti yang ada di Youtube ketika saya sedang mendengarkan playlist lagu saya. Jadi, saya membuat bagian tersebut bisa di-scroll dengan menggunakan property overflow-y: scroll. Properti ini menyebabkan elemen tersebut dapat di-scroll ketika tinggi kumulatif dari semua anak-anak dari elemen itu melebihi tinggi maksimal yang saya tetapkan, yaitu 15rem. Saya juga menerapkankan snapping ke ujung atas dari masing-masing anak elemen ketika elemen tersebut di-scroll. Selain itu, saya juga memberikan ruang kosong di sebelah kanan dari \<section class="hero-skills>"> supaya saya punya ruang tambahan untuk menambahkan bagian lain ke depannya.

3.  Batasan yang saya paling rasakan ketika membuat \<section> baru ini adalah ketika saya harus menambahkan skill   satu per satu. Bayangkan saya jika saya harus menambahkan 20 skill dalam satu waktu. Itu pun belum memperhitungkan panjangnya file .html. Hal itu akan membuat saya kesulitan menambahkan fitur baru untuk web saya. Karena itu, fungsi dinamis yang paling saya inginkan untuk saat ini adalah saya bisa menyimpan data dari skill saya di dalam suatu database sehingga saya tidak perlu mengutak-atik file .html dari web saya.


### AI USAGE

Saya tidak menggunakan AI dalam pembuatan \<section> baru untuk skill pada tugas ini. Saya mencari bagaimana saya melakukan implementasi terhadap ide yang saya punya dengan mencari implementasinya di web W3Schools. Kemudian, saya membaca dokumentasi dari elemen, atribut, dan properti yang digunakan di MDN Web Docs. Contohnya, ketika saya ingin menerapkan scrolling untuk bagian skill baru, saya mencari implementasinya di W3Schools: https://www.w3schools.com/howto/howto_css_menu_horizontal_scroll.asp. Setelah itu, saya membaca dokumentasi dari dua properti yang digunakan, overflow dan white-space, di MDN Web Docs: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow dan https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space. Dari web tersebut, saya jadi menemukan properti yang berkaitan seperti overflow-y yang saya gunakan pada hasil akhir dari tugas ini. Selain dari W3Schools, saya juga membaca dokumentasi dari elemen, atribut, dan properti yang digunakan pada template yang diberikan di tutorial #1. Selain itu, ketika saya sedang membaca MDN Web Docs, terkadang saya menemukan elemen yang menurut saya menarik seperti \<details> dan \<summary> yang juga saya gunakan di hasil akhir tugas.


Sebenarnya saya tidak secara ekstrem menghindari penggunaan AI. Namun, saya berpikir bahwa jika masalah yang saya temukan merupakan masalah yang umum dijumpai orang-orang ketika membuat static web, tentunya ada dokumentasi yang bisa saya baca. Selain menghindari hasil pencarian dari AI yang bisa saja rancu bahkan tidak akurat, saya juga bisa memahami bagaimana suatu elemen, atribut, dan properti dari HTML5 dan CSS secara lebih detail. Selain itu, saya juga tahu darimana saja sumber referensi yang saya gunakan sehingga memudahkan saya dalam membuat daftar referensi yang saya gunakan.


### Referensi

HTML:
- \<a> HTML anchor element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a
- \<details> HTML details disclosure element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details
- \<div> HTML content division element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div
- \<img> HTML image embed element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img
- \<p> HTML paragraph element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p
- \<section> HTML generic section element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section
- \<summary> HTML disclosure summary element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary


CSS:
- :last-child CSS pseudo-class: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child
- align-items CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items
- align-self CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self
- border CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border
- border-radius CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius
- display CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display
- grid-area CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area
- grid-template-areas CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas
- margin CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin
- overflow CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow
- overflow-y CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y
- padding CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding
- scroll-snap-type CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type
- scrollbar-width CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width
- white-space CSS property: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space
- CSS values and units: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units


W3Schools:
- How TO - Horizontal Scroll Menu: https://www.w3schools.com/howto/howto_css_menu_horizontal_scroll.asp
- An image as a link - W#Schools Tryit Editor: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_image












