#Contoh cara menghapus pada Dictionary Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']    #Hapus entri dengan key 'Name'
dict.clear()        #Hapus semua entri di dict
del dict            #Hapus dictionary yang sudah ada

print("dict['Age']:", dict['Age'])
print("dict['School']:", dict['School'])


