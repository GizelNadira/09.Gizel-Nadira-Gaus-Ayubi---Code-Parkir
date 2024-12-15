def hitung_biaya(panjang, lebar, tinggi, berat):
  """
  Fungsi untuk menghitung biaya pengiriman.

  Args:
    panjang: Panjang paket dalam cm.
    lebar: Lebar paket dalam cm.
    tinggi: Tinggi paket dalam cm.
    berat: Berat paket dalam kg.

  Returns:
    Biaya pengiriman dalam rupiah.
  """

  # Periksa dimensi paket
  if panjang <= 50 and lebar <= 50 and tinggi <= 50:
    biaya_per_kg = 5000
  else:
    biaya_per_kg = 7000
    biaya_tambahan = 50000
  
  # Hitung biaya total
  biaya_total = biaya_per_kg * berat + biaya_tambahan
  
  # Pastikan biaya minimal terpenuhi
  if biaya_total < 8000:
    biaya_total = 8000
  
  return biaya_total

# Input data paket
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))

# Hitung biaya pengiriman
biaya = hitung_biaya(panjang, lebar, tinggi, berat)

# Tampilkan hasil
print("Biaya pengiriman:", biaya, "rupiah")