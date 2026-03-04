print("---> PROGRAM PERHITUNGAN BELANJA <---")
hb1 = float(input("Masukan harga barang ke-1 : "))
hb2 = float(input("Masukan harga barang ke-2 : "))
hb3 = float(input("Masukan harga barang ke-3 : "))
total = hb1 + hb2 + hb3
print("Total belanja : ", total)
diskon = 0.05 * total
print("Diskon (5%) : ", diskon)
total_bersih = total - diskon 
print("Harga bersih yang harus dibayar : ", total_bersih)
print("---> TERIMAKASIH <---")