from app import AplikasiPemesanan

def main():
    app = AplikasiPemesanan()
    
    # Menambahkan beberapa event contoh
    app.tambah_event("Konser Sheila On 7", "2023-12-01", 200000, "Konser di Stadion Mandala Krida", 10)
    app.tambah_event("Festival Buku Gramedia", "2023-12-05", 270000, "Konser di Stadion Mandala Krida", 10)
    app.tambah_event("Theater UNJAYA", "2023-12-10", 300000, "Kampus 1", 12)

    while True:
        print("\n" + "=" * 70)
        print("Aplikasi Pemesanan Tiket Event")
        print("=" * 70)
        print("Menu Aplikasi")
        print("1. Menampilkan event yang ada")
        print("2. Memesan tiket")
        print("3. Menampilkan pemesanan")
        print("4. Keluar")
        print("=" * 70)
        
        try:
            pilihan = int(input("Pilih opsi (1-4): "))
            if pilihan == 1:
                app.tampilkan_event()
            elif pilihan == 2:
                app.pesan_tiket()
            elif pilihan == 3:
                app.tampilkan_pemesanan()
            elif pilihan == 4:
                print("Terima kasih! Sampai jumpa.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-4.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()