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
        print("Daftar Event:")
        for i, event in enumerate(self.events):
            print(f"\n{i + 1}. Nama Event: {event.nama}\nTanggal: {event.tanggal}\nHarga: {event.harga}\nDeskripsi: {event.deskripsi}\nStok Tiket: {event.stok}")

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
        print("Daftar Pemesanan:")
        if not self.pemesanan:
            print("Tidak ada pemesanan.")
            return
        for i, tiket in enumerate(self.pemesanan):
            print(f"{i + 1}. {tiket.event.nama} - Jumlah: {tiket.jumlah} - Total Harga: {tiket.jumlah * tiket.event.harga}")
