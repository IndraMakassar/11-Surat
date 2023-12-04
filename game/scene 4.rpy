label scene4:
    ruki "Aku merasa ada yang aneh mengapa ayah tak mengenali Hanako. Padahal Hanako mengatakan bahwa ia pernah bertemu dengan ayah"
    ruki "Dimana lagi aku bisa menemukan informasi tentang Hanako?"
    "Ruki terdiam dan mulai berpikir. Ia kemudian mengingat bahwa Hanako pernah memberikannya hadiah kotak putih, tetapi ia saat memeriksa kamar kemarin ia tidak menemukan kotak itu. Ia memutuskan untuk bertanya kepada bibi di dapur."
    ruki "Permisi Bibi"
    bibi "Iya nona, ada yang bisa saya bantu?"
    ruki "Apakah bibi pernah melihat kotak putih?"
    bibi "Kotak putih? Sepertinya bibi pernah liat, sebentar bibi coba ambilkan digudang"
    "Aku berharap bisa menemukan sesuatu di kotak putih itu"
    bibi "Kotak ini nona?"
    ruki "Hmm sepertinya ia, kotak ini akan saya ambil, terima kasih Bi!"
    "Ruki pergi meninggalkan Bibi di dapur, saat ingin kembali ke kamar Ruki melihat kamar ayahnya tidak terkunci."
    $ isKamarAyah = False
    $ isSimpan = False

    menu kotakPutih:
        "Masuk ke kamar ayah":
            $ isKamarAyah = True
            jump kamarAyah
        "Simpan kotak di kamar":
            $ isSimpan = True
            jump simpanKotak

label kamarAyah:
    scene bg kamar

    ruki "Kamar ini sangat gelap bahkan di siang hari dan bau rokok"
    "Ruki mulai mencari sesuatu di laci dan juga lemari ayahnya tetapi tidak menemukan apapun hingga ia menemukan sebuah kotak di bawah ranjang ayahnya."
    "Kotak itu tidak terkunci dan Ruki memutuskan untuk membukanya dan ternyata didalamnya hanya berisi kertas-kertas biasa saja."
    "Tetapi saat hendak ingin menutupnya ia melihat ada sesuatu yang menempel pada tutup kotak itu. Ia merobek kertas yang menempel pada box tersebut dan menemukan Surat yang persis seperti yang ada di buku harian."
    ruki "Surat ini sama persis seperti yang ada di buku harian, bagaimana bisa surat ini ada di kamar ayah?"
    bibi "Nona, anda dimana? Dokter anda sudah tiba!"
    ruki "Astaga dokter sudah tiba, aku harus segera merapikan ini dan menemui dokter."
    "Ruki pun naik dan menyimpan surat tersebut di kamarnya. Setelah itu Ruki bertemu dengan dokter"
    jump scene5

label simpanKotak:
    scene bg kamar

    "Ruki memutuskan untuk kembali ke kamar menyimpan kotak putih itu"
    bibi "Nona, anda dimana? Dokter anda sudah tiba!"
    ruki "Astaga dokter sudah tiba, aku harus segera merapikan ini dan menemui dokter."
    jump scene5
    
label scene5:
    scene bg kamar

    ruki "Syukurlah dokter mengatakan aku sudah membaik hanya tunggu berapa minggu ingatanku bisa kembali!"
    ruki "Sekarang aku lebih baik segera naik kekamarku"
    "Ruki segera keatas dan membuka kotak putih itu. Kotak putih itu berisi liontin dan beberapa surat. Ia kemudian membuka beberapa surat itu!"
    """
    Tanggal 28 September
    \nPAMANMU SUDAH KEMBALI? Aku tidak percaya jika dia sudah berubah, aku rasa ia mencari bukti yang kita sembunyikan. Apakah kau ingin aku membawanya ke pihak berwajib? 
    
    Ya walaupun kita tidak tau isi amplop merah itu

    Tanggal 30 September 2023
    \nBaiklah, aku tidak akan mengambil amplop itu, aku akan menunggu arahan dari mu dan akupun tidak bisa memaksamu untuk menjauh dari pamanmu. 
    
    Tapi apakah kau punya rencana lain?
    """
    ruki "jadi benar semua ini ada kaitannya dengan amplop merah. Tapi bukti apa yang ada di amplop merah?"
    ruki "Liontin ini untuk ku? Atau aku dulu pernah menggunakannya? Ah ternyata bisa terbuka! Hmm hanya terdapat fotoku tetapi foto ini terlihat seperti dirobek?"

    if isKamarAyah==True:
        jump sceneAfterKamar
    else:
        jump afterKotak

label sceneAfterKamar:
    scene bg kamar

    "Kemudian Ruki membuka surat yang ia temukan di kamar ayahnya"
    """
    Tanggal 25 September 
    \nHai Ruki! Hahaha Baiklah kita akan mencari waktu untuk datang ke tempat itu! Aku rasa kau juga tidak bisa melupakannya. Ohiyah terkait code yang kau bicarakan tentu saja aku masih ingat! 
    
    Kau tau bukan yang mengetahui code ini hanya kita? Dan akupun sudah berjanji tidak akan memberi tahu siapapun tentang amplop itu 

    Tanggal 8 November 2023
    \nRuki! Mengapa kau tidak membalas suratku? Apakah kau baik-baik saja? Aku sangat khawatir sekarang! Aku tau aku nekat tetapi aku benar-benar bingung, jadi jangan memarahiku nanti. 
    
    Aku memutuskan untuk mendatangimu ini malam.
    """
    ruki "Code apa yang dimaksud? apakah amplop yang dimaksud adalah amplop yang ayah cari selama ini?"
    ruki "Apa yang sebenarnya terjadi padaku hingga aku tidak membalas surat Hanako? Ahk aku benar-benar tidak bisa mengingat apapun!"
    ruki "Jika surat ini ayah simpan berarti ia mengetahui jika Hanako datang saat itu…"
    jump scene7

label afterKotak:
    "Ruki semakin penasaran dan memutuskan untuk kembali ke kamar ayahnya."
    jump kamarAyah2

label kamarAyah2:
    ruki "Kamar ini sangat gelap bahkan di siang hari dan bau rokok"
    "Ruki mulai mencari sesuatu di laci dan juga lemari ayahnya tetapi tidak menemukan apapun hingga ia menemukan sebuah kotak di bawah ranjang ayahnya."
    "Kotak itu tidak terkunci dan Ruki memutuskan untuk membukanya dan ternyata didalamnya hanya berisi kertas-kertas biasa saja."
    "Tetapi saat hendak ingin menutupnya ia melihat ada sesuatu yang menempel pada tutup kotak itu. Ia merobek kertas yang menempel pada box tersebut dan menemukan Surat yang persis seperti yang ada di buku harian."
    ruki "Surat ini sama persis seperti yang ada di buku harian, bagaimana bisa surat ini ada di kamar ayah?"
    jump sceneAfterKamar