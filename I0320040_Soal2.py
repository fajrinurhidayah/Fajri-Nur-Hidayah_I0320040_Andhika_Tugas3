#dictionary nama, hobi, sosial media, lagu, dan makanan favorit
print('Dictionary berisi nama, hobi, sosial media, lagu, dan makanan favorit')
dict = {'Nama' : ['Fajri Nur Hidayah'],
        'Hobi' : ['Menonton anime', 'tidur', 'menyanyi'],
        'Sosial Media' : ['Instagram : @fajrin.hdy', 'Twitter : @asdfghjkl', 'Picsart : @fajrinh'],
        'Lagu Favorit' : ['Stay With Me-Miki Matsubara(Cover by Chris Andrian)', 'Kokoronashi', 'Gurenge'],
        'Makanan Favorit' : ['Mi ayam', 'Rendang', 'Sate']}
print(dict)

#Mengubah satu hobi
dict['Hobi'][2]=('jalan-jalan')

#Mengubah satu sosial media
dict['Sosial Media'][1]=('Linkedin : Fajri Nur Hidayah')

#Menghapus dua makanan favorit
del dict['Makanan Favorit'][1:3]

#Menambah satu hobi
dict['Hobi'].append('Makan')
print(dict)


