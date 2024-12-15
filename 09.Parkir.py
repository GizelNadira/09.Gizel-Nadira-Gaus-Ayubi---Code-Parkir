def hitung_biaya_parkir_terminal(durasi):
    if durasi <= 2:
        return 3000
    else:
        biaya = 3000 + (durasi - 2) * 1500
        
        if durasi > 24:
            biaya += 10000
        
        return biaya

# Input durasi parkir
durasi = int(input("Masukkan durasi parkir (jam): "))

biaya = hitung_biaya_parkir_terminal(durasi)
print(f"Biaya parkir: Rp {biaya}")