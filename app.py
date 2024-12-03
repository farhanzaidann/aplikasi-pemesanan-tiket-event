class Event:
    def __init__(self, nama, tanggal, harga, deskripsi, stok):
        self.nama = nama
        self.tanggal = tanggal
        self.harga = harga
        self.deskripsi = deskripsi
        self.stok = stok

class Tiket:
    def __init__(self, event, jumlah, nama, no_hp, email):
        self.event = event
        self.jumlah = jumlah
        self.nama = nama
        self.no_hp = no_hp
        self.email = email

class AplikasiPemesanan:
    def __init__(self):
        self.events = []
        self.pemesanan = []

    def tambah_event(self, nama, tanggal, harga, deskripsi, stok):
        event = Event(nama, tanggal, harga, deskripsi, stok)
        self.events.append(event)

    def tampilkan_event(self):
        print("\n" + "=" * 70)
        print("Daftar Event:")
        print("=" * 70)
        print(f"{'No.':<5} {'Nama Event':<25} {'Tanggal':<15} {'Harga':<10} {'Stok':<10}")
        print("=" * 70)
        for i, event in enumerate(self.events):
            print(f"{i + 1:<5} {event.nama:<25} {event.tanggal:<15} {event.harga:<10} {event.stok:<10}")
        print("=" * 70)
        print(" ")

    def pesan_tiket(self):
        self.tampilkan_event()
        try:
            pilihan = int(input("Pilih event (nomor): ")) - 1
            if 0 <= pilihan < len(self.events):
                jumlah = int(input("Jumlah tiket yang ingin dipesan: "))
                event = self.events[pilihan]
                nama = input("Nama Pemesan: ")
                no_hp = int(input("No HP Pemesan: "))
                email = input("Email Pemesan: ")
                harga = event.harga * jumlah
                print("=" * 70)

                if jumlah > event.stok:
                    print(f"Stok tidak mencukupi. Tersedia hanya {event.stok} tiket.")
                else:
                    tiket = Tiket(event, jumlah, nama, no_hp, email)
                    self.pemesanan.append(tiket)
                    event.stok -= jumlah  # Mengurangi stok tiket
                    print(f"Tiket untuk {event.nama} sebanyak {jumlah} telah dipesan oleh:")
                    print(f"Nama: {nama}\nNo HP: {no_hp}\nEmail : {email}\nHarga: Rp.{harga}")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    def tampilkan_pemesanan(self):
        print("\n" + "=" * 70)
        print("Struk Tiket:")
        print("=" * 70)
        if not self.pemesanan:
            print("Tidak ada pemesanan.")
            print("=" * 70)
            return

        for i, tiket in enumerate(self.pemesanan):
            total_harga = tiket.jumlah * tiket.event.harga
            print(f"{'Nama Event:':<15} {tiket.event.nama}")
            print(f"{'Jumlah:':<15} {tiket.jumlah}")
            print(f"{'Total Harga:':<15} {total_harga}")
            print(f"{'Nama Pemesan:':<15} {tiket.nama}")  
            print(f"{'No HP:':<15} {tiket.no_hp}")
            print(f"{'Email:':<15} {tiket.email}")
            print("=" * 70)