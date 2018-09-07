table_eggnog = open('eggnog_filter.csv', 'r')
turtle_eggnog = open('turtle_eggnog.ttl', 'w')

prefix = ('@base <http://eggnog.org/> .\n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n' +
    '@prefix eggnog_core: <http://eggnog.org/> .\n@prefix uniprot_core: <http://purl.uniprot.org/core/> .')

turtle_eggnog.write(prefix + '\n\n')

for line in table_eggnog:
    line = line.strip().split('\t')
    if 'Group Name' not in line:
        eggnog = '<' + line[1] + '> a eggnog_core:' + line[0] + ' ;'
        group_name = '\teggnog_core:groupName eggnog_core:' + line[1] + ' ;'
        protein_count = '\teggnog_core:proteinCount \"' + line[2] + '\" ;'
        species_count = '\teggnog_core:speciesCount \"' + line[3] + '\" ;'
        cog_functional = '\teggnog_core:COGFunctional \"' + line[4] + '\" ;'
        consensus_description = '\teggnog_core:consensusDescrition \"' + line[5] + '\" ;'
        members = line[6].split(',')
        functional_category = '\teggnog_core:functionalCategory \"' + line[7] + '\" ;'
        uniprot_id = '\tuniprot_core:idUniprot uniprot_core:' + line[8] + ' .'
        turtle_eggnog.write(eggnog + '\n' + group_name + '\n' + protein_count + '\n' + 
            species_count + '\n' + cog_functional + '\n' + consensus_description + '\n')
        #for member in members:
        #    turtle_eggnog.write('\teggnog_core:groupMembers eggnog_core:' + member + ' ;\n')
        turtle_eggnog.write(functional_category + '\n' + uniprot_id + '\n\n')
    else:
        pass