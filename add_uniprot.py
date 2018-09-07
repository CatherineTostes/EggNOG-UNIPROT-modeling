# -*- coding: utf-8 -*-
# Catherine dos Santos Tostes
#

from time import strftime

print("Init Reading and Processing")
print(strftime('%H:%M:%S'))

# Init reading and preparating of the files

file_filtered = open('eggnog_filtered_new.csv', 'r')
file_id_uniprot = open('uniprot_id.csv', 'r')
file_filtered_new = open('eggnog_filter.csv', 'w')

print('Adding IDs in Dictionary')
print(strftime('%H:%M:%S'))

# Adding in the dictionary the keys and the value with the ID Uniprot and ID group EggNOG

eggnog_uniprot = {}

for eggnog in file_id_uniprot:
    eggnog = eggnog.strip().replace('\t', ';').split(';')
    if eggnog[0] not in eggnog_uniprot:
        eggnog_uniprot[eggnog[0]] = eggnog[1].strip()
    else:
        pass

print('Adding ID Uniprot in file_filtered')
print(strftime('%H:%M:%S'))

# Checking the ID EggNog for adding ID Uniprot

for line in file_filtered:
    id_eggnog = line.strip().split(';')[1]
    if id_eggnog in eggnog_uniprot.keys():
        content = line.strip() + ';' + eggnog_uniprot[id_eggnog] + '\n'
        file_filtered_new.write(content)

print('Finish')
print(strftime('%H:%M:%S'))
