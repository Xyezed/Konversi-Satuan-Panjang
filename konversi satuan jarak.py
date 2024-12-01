def KonversiSatuanJarak(nilai, dari_unit, ke_unit):
    Tangga  = {
        'mm': 0.001,   
        'cm': 0.01,   
        'dm': 0.1,    
        'm': 1,        
        'dam': 10,     
        'hm': 100,     
        'km': 1000,    #
    }
    if dari_unit not in Tangga or ke_unit not in Tangga:
        raise ValueError("Satuan tidak valid. Gunakan mm, cm, dm, m, dam, hm, atau km.")

    selisih = nilai * Tangga[dari_unit]

    nilai_konversi = selisih / Tangga[ke_unit]
    return nilai_konversi

nilai = float(input("Masukkan Nilai : "))  # Nilai yang akan dikonversi
dari_unit = input('Masukkan satuan asal : ')
ke_unit = input('Masukkan satuan tujuan : ')

hasil = KonversiSatuanJarak(nilai, dari_unit, ke_unit)
print(f"{nilai} {dari_unit} = {hasil} {ke_unit}")

#Xyezed 

