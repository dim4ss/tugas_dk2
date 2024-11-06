# main.py

#fungsi untuk memeriksa apakah input adalah bilangan pasitif 
def input_positif(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai > 0:
                return nilai
            else:
                print("Nilai harus lebih dari 0. coba lagi.")
        except ValueError:
            print("Input tidak valid.masukan angka.")

#meminta input panjang dan lebar dari pengguna
Panjang = float(input("masukan panjang persegi panjang:"))
Lebar = float(input("masukan lebar persegi panjang:"))

#menghitung luas
Luas = Panjang * Lebar

#menghitung keliling

#menampilkan hasil luas
keliling = 2 * (Panjang + Lebar )

#menampilkan hasil luas dan keliling
print(f"Luas persegi panjang: {Luas} satuan persegi")
print(f"Keliling persegi panjang adalah: {Keliling} satuan")