class Event:
    def __init__(self, nama, tanggal, harga, deskripsi, stok):
        self.nama = nama
        self.tanggal = tanggal
        self.harga = harga
        self.deskripsi = deskripsi
        self.stok = stok


class Tiket:
    def __init__(self, event, jumlah):
        self.event = event
        self.jumlah = jumlah

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

    def pesan_tiket(self):
        self.tampilkan_event()
        try:
            pilihan = int(input("Pilih event (nomor): ")) - 1
            if 0 <= pilihan < len(self.events):
                jumlah = int(input("Jumlah tiket yang ingin dipesan: "))
                event = self.events[pilihan]

                if jumlah > event.stok:
                    print(f"Stok tidak mencukupi. Tersedia hanya {event.stok} tiket.")
                else:
                    tiket = Tiket(event, jumlah)
                    self.pemesanan.append(tiket)
                    event.stok -= jumlah  # Mengurangi stok tiket
                    print(f"Tiket untuk {event.nama} sebanyak {jumlah} telah dipesan.")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    def tampilkan_pemesanan(self):
        print("\n" + "=" * 70)
        print("Daftar Pemesanan:")
        print("=" * 70)
        if not self.pemesanan:
            print("Tidak ada pemesanan.")
            print("=" * 70)
            return
        print(f"{'No.':<5} {'Nama Event':<25} {'Jumlah':<10} {'Total Harga':<15}")
        print("=" * 70)
        for i, tiket in enumerate(self.pemesanan):
            total_harga = tiket.jumlah * tiket.event.harga
            print(f"{i + 1:<5} {tiket.event.nama:<25} {tiket.jumlah:<10} {total_harga:<15}")
        print("=" * 70)
