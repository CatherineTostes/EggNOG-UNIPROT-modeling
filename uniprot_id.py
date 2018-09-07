# -*- coding: utf-8 -*-
# Catherine dos Santos Tostes
#

import requests
from bs4 import BeautifulSoup
import re
from time import strftime

# Prepariting files for reading or writing of th results

def handle(path, mode, content=None):
    file = open(path, mode)
    if ((mode == 'r') or (mode == 'rb')):
        content = file.read()
        file.close()
        return(content)
    else:
        file.write(content)
        file.close()

# Uniprot search function with uniprot id keys from table EggNOG

def uniprot_search(uniprot_id):
    url = 'https://www.uniprot.org/uniprot/'
    uniprot_id = uniprot_id
    search = requests.get(url + uniprot_id)
    soup = BeautifulSoup(search.content, 'html.parser')
    annotation = soup.title.text
    annotation = annotation.strip().split('-')
    gene = annotation[0].strip()
    protein = soup.h1.text
    organism = soup.em.text
    h = soup.findAll('a', attrs={'href': re.compile("^/taxonomy/")})[7].text
    t = soup.findAll('a', attrs={'href': re.compile("^/taxonomy/")})[8].text
    host = h + ' [TaxID: '+ t + ']'
    return(gene + ';' + protein + ';' + organism + ';' + host)

print("Init Reading and Processing")
print(strftime('%H:%M:%S'))

# Init reading and preparating of the files

file_id_uniprot = open('uniprot_id.csv', 'r')
new_file = open('uniprot_organism.csv', 'w')

# Create new spreadsheet with Uniprot information

print('Uniprot information')
print(strftime('%H:%M:%S'))

for key in file_id_uniprot:
    try:
        key = key.strip().replace('\t', ';')
        eggnog_id = key.strip().split(';')[0]
        uniprot_id = key.strip().split(';')[1]
        rst = uniprot_search(uniprot_id)
        rst = rst.strip()
        content = (uniprot_id + ';' + eggnog_id + ';' + rst + '\n')
        print(content)
        new_file.write(content)
    except:
        pass