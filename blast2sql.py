

import sys

def main():


	with open(sys.argv[1], 'r') as rfile:
		lines = []
		for line in rfile:
			lines.append(line.rstrip('\n').split('\t'))

		# print(lines[0])


	for i in range(len(lines)):
		scov = float(lines[i][8])/float(lines[i][3])
		lines[i].append(scov)

		lines[i][1] = lines[i][1][4:-1]


	# print(lines[0])
	# print(len(lines[0]))

	for i in lines:

		print "INSERT INTO blast1 (qseqid, sseqid, qlen, slen, bitscore, evalue, pident, nident, length, qcovs, qstat, qend, sstart, scov) VALUES ("+'\''+i[0]+'\',\''+i[1]+'\','+i[2]+','+i[3]+','+i[4]+','+i[5]+','+i[6]+','+i[7]+','+i[8]+','+i[9]+','+i[10]+','+i[11]+','+i[12]+','+str(i[13])+");" 


	# qseqid, sseqid, qlen, slen, bitscore, evalue, pident, nident, length, qcovs, qstat, qend, sstart, scov



if __name__ == "__main__":
	main()
