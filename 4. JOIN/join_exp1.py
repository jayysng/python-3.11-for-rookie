# Buat dulu 2 dictionary sebagai contoh tabelnya:
table1 = [
    {'ID': 1, 'Name': 'Alice'},
    {'ID': 2, 'Name': 'Bob'},
    {'ID': 3, 'Name': 'Charlie'}
]

table2 = [
    {'ID': 2, 'Age': 25},
    {'ID': 3, 'Age': 30},
    {'ID': 4, 'Age': 22}
]

# Lakukan INNER JOIN berdasarkan kolom 'ID'
result_inner = [dict(item1, **item2) for item1 in table1 for item2 in table2 if item1['ID'] == item2['ID']]
print("INNER JOIN:")
print(result_inner)

# Lakukan LEFT JOIN berdasarkan kolom 'ID'
result_left = [dict(item1, **item2) if item1['ID'] == item2['ID'] else item1 for item1 in table1 for item2 in table2]
print("\nLEFT JOIN:")
print(result_left)

# Lakukan RIGHT JOIN berdasarkan kolom 'ID'
result_right = [dict(item1, **item2) if item1['ID'] == item2['ID'] else item2 for item1 in table1 for item2 in table2]
print("\nRIGHT JOIN:")
print(result_right)

# Lakukan OUTER JOIN berdasarkan kolom 'ID'
result_outer = result_left + [item2 for item2 in table2 if item2 not in result_left]
print("\nOUTER JOIN:")
print(result_outer)

#done
