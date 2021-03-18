#List teman
list_teman = ['Desy', 'Denny', 'Erika', 'Yola', 'Zaneta', 'Vizal', 'Maurich', 'Efa', 'Afiq', 'Athan' ]

#isi list index no. 4, 6, 7.
print('Teman pada index no. 4, 6, 7 : ', list_teman[4], list_teman[6], list_teman[7])

#Mengganti nama teman berindex 3, 5, 9.
list_teman[3] = 'Sekar'
list_teman[5] = 'Nadya'
list_teman[9] = 'Amar'

#Menambah 2 nama teman
list_teman.append('Anisa')
list_teman.append('Erysa')

#Menampilkan semua nama teman dengan perulangan
print('Perulangan list teman :', (list_teman*3))

#Menampilkan panjang list
print('Panjang list teman :', len(list_teman))



