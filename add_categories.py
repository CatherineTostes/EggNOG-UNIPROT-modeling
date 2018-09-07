# -*- coding: utf-8 -*-
# Catherine dos Santos Tostes
#

# Prepariting files for reading or writing of th results

from time import strftime

print("Init Reading and Processing")
print(strftime('%H:%M:%S'))

# Init reading and preparating of the files

file_filtered = open('eggnog_filtered.csv', 'r')
file_categories = open('file_categories.csv', 'r')
file_filtered_new = open('eggnog_filtered.csv', 'w')

print('Adding Functional Categories in Dictionary')
print(strftime('%H:%M:%S'))

# Adding in the dictionary the keys and the value with the symbols and their functional categories

categories = {}

for line in file_categories:
    line = line.strip().split(';')
    if line[0] not in categories:
        categories[line[0]] = line[1].strip()
    else:
        categories[line[0]].append(line[1]).strip()

print('Adding name of the functional categories')
print(strftime('%H:%M:%S'))

# Checking the symbol line of the file_filtered column of the functional categories to retrieve its name

for line in file_filtered:
    symbol = line.strip().split(';')[4]
    if symbol in categories.keys():
        content = line.strip() + ';' + categories[symbol] + '\n'
        file_filtered_new.write(content)

print('Finish')
print(strftime('%H:%M:%S'))