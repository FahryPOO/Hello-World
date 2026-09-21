user = input("masukkan nama pelanggan :")
time = int(input("waktu bermain :"))
harga_sewa_perjam = float(5000)
harga = harga_sewa_perjam * time
if time > 8:
    harga = harga - (harga * 10/100)
elif time >= 5:
    harga = harga - (harga * 5/100)
else:
    harga = harga

print("======= Struktur Sewa Pc =======")
print("nama         :", user)
print("Lama main    :", time, "jam")
print("Harga perjam :", harga_sewa_perjam, "Rupiah")
print("Harga bayar  :", harga, "Rupiah")