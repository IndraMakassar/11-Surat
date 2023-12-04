screen black_screen(text):
    # Use a black frame to fill the whole screen
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1.0
        ysize 1.0
        background "#000"
        # Use a text widget to display the text
        text text color "#fff" align (0.5, 0.5)


label scene10:    
    scene black
    show screen black_screen("3 bulan kemudian")
    ""
    ruki "Hari ini aku akan datang ke toko buku dan bertemu dengan Takhi"

    hide screen black_screen

    scene bg toko buku

    ruki "Hai Tahki apakah kau sudah makan? Aku membawakanmu makan siang"
    takhi "Wah Pacar aku memang paling pengertian, akan aku makan nanti setelah merangkum ini semua. Terima kasih sayang"
    
    "Ruki Pun tersenyum dan mulai menuju ke rak-rak buku. Tatapannya berhenti pada satu buku yang tak Asing yaitu buku Girl in the dark, ia mengambil buku itu dan membuka halamanya dan menemukan surat."

    """
    Hai Hanako!
    \nAku tau kau bakal menemukan surat ini. Surat ini adalah surat rahasia kedua untukmu, hahaha bercanda surat ini sengaja kutulis dan berharap suatu saat kau menemukannya!
    
    Aku hanya ingin bilang terima kasih karena telah menjadi sahabat sekaligus saudara untukku. Kau tau, kau sangat berharga untukku jadi jangan pernah meninggalkanku yah. 
    
    Oh iya, aku berharap kau menyukai liontin yang berisi foto kita, aku sengaja agar kau bisa selalu mengingatku.

    Hanako belakangan ini perasaanku tidak enak, aku merasa seperti akan pergi jauh tapi entah kemana, aku takut terjadi sesuatu dengan ku, Jika ternyata sesuatu kepadaku berjanjilah untuk selalu bahagia dan jagakan Takhi untukku.

    """
    "Aku menyayangimu…
    \naku berharap Takhi tidak menemukan surat ini, aku akan sangat malu jika dia menemukannya.
    \n-- love Ruki"

    "Ruki Hanya tersenyum dan…
    \n“Kau tenang saja Ruki, Takhi tentu saja akan bahagia bersamaku”"

    