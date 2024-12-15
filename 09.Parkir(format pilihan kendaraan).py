#!/usr/bin/python3

def hitung_durasi(jam_keluar, jam_masuk):
    """
    Menghitung durasi parkir.

    Args:
        jam_keluar (int): Jam keluar parkir.
        jam_masuk (int): Jam masuk parkir.

    Returns:
        int: Durasi parkir.

    Raises:
        ValueError: Jika durasi parkir tidak valid.
    """
    durasi = jam_keluar - jam_masuk
    
    if durasi < 0:
        raise ValueError('Durasi Tidak Valid!!')
    return durasi

def hitung_biaya_parkir(jam_keluar, jam_masuk, jenis_kendaraan):
    """
    Menghitung biaya parkir.

    Args:
        jam_keluar (int): Jam keluar parkir.
        jam_masuk (int): Jam masuk parkir.
        jenis_kendaraan (str): Jenis kendaraan.

    Returns:
        str: Informasi tentang durasi parkir dan biaya parkir.
    """
    # Tarif kendaraan per jam
    tarif_parkir = {
        'Mobil': 2000,
        'Sepeda': 1000,
        'Truk': 3000,
        'Bus': 5000
    }

    # Biaya tambahan setelah parkir 24 jam
    biaya_tambahan = 5000

    # Hitung durasi
    try:
        durasi = hitung_durasi(jam_keluar, jam_masuk)
    except ValueError as e:
        return str(e)

    # Cek validasi jenis kendaraan
    if jenis_kendaraan not in tarif_parkir:
        return 'Jenis Kendaraan tidak Valid!!'

    # Hitung biaya parkir
    biaya = durasi * tarif_parkir[jenis_kendaraan]

    # Tambahkan biaya tambahan jika parkir lebih dari 24 jam
    if durasi > 24:
        biaya += biaya_tambahan

    return f'Durasi Parkir Anda: {durasi} jam, Biaya Parkir {jenis_kendaraan}: Rp{biaya}'

def main():
    try:
        jam_masuk = int(input('Masukkan jam masuk Anda (dengan format 24 jam): '))
        jam_keluar = int(input('Masukkan jam keluar Anda (dengan format 24 jam): '))
        jenis_kendaraan = input('Pilih jenis kendaraan Anda (Mobil/Sepeda/Truk/Bus): ').capitalize()

        print(hitung_biaya_parkir(jam_keluar, jam_masuk, jenis_kendaraan))
    except ValueError:
        print('Input (Masukan) Harus Berupa Angka!!')

if __name__ == "__main__":
    main()