table_uniprot = open('uniprot_organism.csv', 'r')
turtle_uniprot = open('turtle_uniprot.ttl', 'w')

prefix = ('@base <http://purl.uniprot.org/uniprot/> .\n@prefix uniprot_core: <http://purl.uniprot.org/core/> .\n' +
    '@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n' +
    '@prefix enog_core: <http://eggnog.org/> .')

turtle_uniprot.write(prefix + '\n\n')

for line in table_uniprot:
    line = line.strip().split(';')
    uniprot = '<' + line[0] + '> a uniprot_core:Protein ;'
    id_uniprot = '\tuniprot_core:idUniprot \"' + line[0] + '\" ;'
    group_name = '\tuniprot_core:groupName enog_core:' + line[1] + ' ;'
    gene = '\tuniprot_core:locusName \"' + line[2] + '\" ;'
    protein = '\tuniprot_core:fullName \"' + line[3] + '\" ;'
    organism = '\tuniprot_core:organism \"' + line[4] + '\" ;'
    tax = '\tuniprot_core:taxID \"' + line[5] + '\" .'
    turtle_uniprot.write(uniprot + '\n' + id_uniprot + '\n' + group_name + '\n' + gene + '\n' + protein + '\n' + organism + '\n' + tax + '\n\n')