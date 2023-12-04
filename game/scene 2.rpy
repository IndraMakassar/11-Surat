
label pilihKamar:
    menu:
        "Mulai mencari petunjuk di kamar":
            if isKamar==True:
                jump pilihKamar
            else:
                $ isKamar = True
                jump kamar
        "Mulai mencari petunjuk di ruang keluarga":
            if isRuangKeluarga==True:
                jump pilihKamar
            else:
                $ isRuangKeluarga = True
                jump ruangKeluarga
    return

label scene2:
    
    scene bg kamar
    with Dissolve(10)

    "Langit sudah gelap, Ruki terbangun dari tidurnya dan mulai melihat sekelilingnya dan ia menyadari bahwa ia masih berada di tempat yang sama."
    "Wah… aku masih di tempat ini, tetapi badanku sudah tak terasa sakit lagi. Aku rasa aku perlu mencari tau apa yang sebenarnya terjadi tapi mulai dari mana yah"
    $ isRuangKeluarga = False
    $ isKamar = False
    jump pilihKamar
    return

label kamar:

    scene bg kamar
    with Dissolve(10)

    ruki "kamar ini terlihat sangat rapi dan penuh dengan buku-buku, apakah dulu aku sangat menyukai buku"
    "mengambil salah satu buku"
    ruki "Hmm tidak ada informasi atau apapun yang bisa kudapatkan, tidak ada foto ataupun catatan tentang diriku. Aku makin penasaran bagaimana bisa aku kehilangan ingatanku"
    ruki "Tunggu, buku apa ini? buku ini terlihat sangat berbeda dengan yang lain."
    # "membuka buku"
    ruki "wah ini semacam buku harian, tapi aneh ada tulisan di halaman depanya “Jangan percaya siapapun selain ayah” apa maksudnya ini?"
    ruki "Aku baru saja mendapatkan petunjuk  tapi sudah membuatku pusing saja, eh tapi kok banyak amplop didalamnya"

    """
    Tanggal 22 September 2023\nHai Ruki!
    Apa kabar? Aku harap kau baik-baik saja, oh iya aku ada kabar baik untukmu, aku akan segera balik, jadi Tunggu aku yah!\n
    -  Hanako {\rt}
    """

    """
    Tanggal 18 Oktober 2023\nHai Ruki!
    Syukurlah kau baik-baik saja, aku juga baik kok. Tentu saja, Aku sangat senang karena akhirnya aku bisa kembali ke rumah, Ngomong-ngomong apa Kau ingat? 
    
    saat pertama kali kita ketemu di toko buku, saat itu sangat seru, kalau kau punya waktu mungkin kita bisa mendatangi tempat itu lagi!\n
    - Hanako
    """

    ruki "Surat ini untukku? Tapi aku tidak bisa mengingat siapa Hanako?"

    """
    Tanggal 20 Oktober 2023\nHai Ruki! 
    Keadaanku juga baik! Ouh tidak masalah jika kau tak bisa, aku bisa mengerti kondisi keluargamu, tapi kau baik-baik sajakan? 
    
    Jika terjadi sesuatu jangan lupa untuk mengabariku!\n
    - Hanako
    """

    """
    Tanggal 22 Oktober 2023\nHai Ruki!
    Syukurlah jika kau baik-baik saja! Ohiyah aku habis dari toko buku, tempat itu tidak berubah sama sekali, suasana dan baunya masih sama dan terpenting 
    
    Dia masih ada disitu dan dia mencarimu! Hahaha aku rasa dia masih menunggumu!\n
    - Hanako
    """

    ruki "Hmm tidak ada yang menarik dari surat ini, tapi aku menjadi penasaran siapa Hanako dan dia yang ia maksud di toko buku, eh masih ada satu surat lagi!"

    """
    Tanggal 2 November 2023\nHai Ruki
    Selamat Ulang tahun sahabatku! Maaf aku tidak bisa mengucapkannya secara langsung. Kemarin aku nekat untuk mendatangi rumahmu dan aku bertemu dengan ayahmu. 
    
    Ayahmu mengatakan kau sedang tidak sehat dan menyuruhku untuk pulang. Mungkin karena aku menggunakan masker dan topi jadi terlihat aneh dan misterius!

    mungkin nanti aku aku akan datang lebih rapi lagi dan bisa memperkenalkan diriku dengan baik! Ohiyah aku sudah menitip kadoku kotaknya berwana putih apakah kau sudah menerimanya?\n- Hanako
    """

    ruki "Wah ternyata dia pernah berusaha datang ke rumah ini, mungkin akan ku tanyakan besok kepada Ayah." 

    if isRuangKeluarga==False:
        jump pilihKamar
    else:
        jump scene3

label ruangKeluarga:

    scene bg ruang keluarga

    ruki "Rumah ini cukup besar tetapi terlihat sangat sepi, dimana yah semua orang?"    
    ayah "Ruki?"
    ruki "Iya?"
    ayah "Apakah sudah baikan?"   
    ruki "Iya, hanya saja aku benar-benar tidak bisa mengingat apapun."
    ayah "Apa kau sungguh lupa ingatan? atau kau hanya pura-pura?"
    ruki "Maksudnya?"
    ayah "Ah sudahlah lupakan saja, apa yang kau lakukan disini? Tunggu ayah ingin bertanya apakah kau pernah melihat amplop merah?"
    ruki "Tidak, aku bahkan tak mengingat apapun tentang amplop merah. Apa amplop itu penting?"
    ayah "Penting, tetapi amplop itu hanya berisi berkas-berkas kantor ayah, jika kau melihat kau bisa berikan kepada ayah"
    ruki "Baiklah"
    # TODO pecah kalimatnya jadi pendek
    "Sepertinya amplop itu sangat penting untuk ayah, tetapi kenapa ayah bertingkah sangat aneh dan mempertanyakan apakah aku berpura-pura. padahal jelas-jelas aku tidak bisa mengingat apapun. Ah sudahlah aku akan kembali ke kamar."
    if isKamar==False:
        jump pilihKamar
    else:
        jump scene3