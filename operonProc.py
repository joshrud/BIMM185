'''
Josh Rudolph
BIMM185
creates the sql insert statements for the operons table and operons_bygene table


'''



import sys

with open(sys.argv[1], 'r') as rfile:
	data = []
	for line in rfile:
		if line[0] == '#':
			continue
		else:
			data.append(line.replace('[','').replace(']','').rstrip('\n').split('\t'))

for i in data:
	for j in i:


		if '\'' in j:
			# print(i)
			j.replace('\'', '')
		# elif "'" in j:
		# 	print(i)
		# 	j.replace("'", '')
		elif '"' in j:
			print(i)
			j.replace('"', '')



# for i in data:
# 	for j in i[5].split(','):
# 		print "INSERT INTO operons_bygene_5_23 (name, start, end, strand, num_genes, genes_contained, evidence, evidence_support) VALUES ("+'\''+i[0]+'\','+str(i[1])+','+str(i[2])+',\''+i[3]+'\','+str(i[4])+',\''+j+'\',\''+i[6]+'\',\''+i[7]+'\''+");" 

for i in data:
	print "INSERT INTO operons_5_23 (name, start, end, strand, num_genes, genes_contained, evidence, evidence_support) VALUES ("+'\''+i[0]+'\','+str(i[1])+','+str(i[2])+',\''+i[3]+'\','+str(i[4])+',\''+j+'\',\''+i[6]+'\',\''+i[7]+'\''+");" 
