#Practice Compare and Logic

print("====PROGRAM====")
print('\n')

ALTERNATIF 1
z = float(input("masukkan angka: "))
x = z > 0 and z < 5 or z > 8 and z < 11
y = z < 0 and z > 5 or z < 8 and z > 11

hasil = x and y
hasil2 = x or y
print("Hasil angka x-nya adalah = ",x)
print("Hasil angka y-nya adalah = ",y)
print("Hasil irisan x dan y adalah = ",hasil)
print("Hasil gabungan x dan y adalah",hasil2)

# ALTERNATIF 2

z = float(input("masukkan angka: "))

assign  = z > 0
assign2 = z < 5
assign3 = z > 8
assign4 = z < 11
assign5 = assign and assign2 or assign3 and assign4
print("Hasil rentang angka :", assign5)

# ALTERNATIF 3

z = float(input("masukkan angka: "))

assign = 0 < z < 5 or 8 < z < 11
print("Hasil rentang angka :", assign)

b = 9

c = ~ b

print('\nNilai b:',b,' dalam bentuk binary:', format(b, '08b'))
print('---------------------------------------( ~ )')
print('Nilai c:',c,' dalam bentuk binary:', format(c & 0xFF, '08b'))


