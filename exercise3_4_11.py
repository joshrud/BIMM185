"""
+
+	Josh Rudolph
+	BIMM185
+	Exercise3 from class
+	INPUT: takes in 1 sequence file and 1 start/stop positioning file for proteins
+	OUTPUT: creates a file "outputex3.txt" that holds the table of number of occurrences of each codon,
+		labeled by each sequence's locus number, then the length of that sequence. 
+	exercise3_4_11.py
+	
+
+
"""

import textwrap
import itertools
from collections import defaultdict

# take in data from sequencing file (filled with nucleotides)
print("TAKING IN FILE1 DATA...")
with open("GCF_000005845.2_ASM584v2_genomic.fna", "r") as rfile:
	
	lines = []
	for line in rfile:
		lines.append(line.rstrip('\n'))
	
# print(lines[:10])
data = "".join(lines)
# print(data[:10])
data = data[71:]
# print(data[:50])
print("...DONE")

# take in data from table describing each protein at a specific destination in GCF file
print("TAKING IN FILE2 DATA...")
with open("proteinTable.txt", "r") as rfile2:
	
	next(rfile2)
	starts = []
	stops = []
	loci = []
	for line in rfile2:

		if line == '\n':
			continue

		starts.append(line.rstrip('\n').split('\t')[2])
		stops.append(line.rstrip('\n').split('\t')[3])
		loci.append(line.rstrip('\n').split('\t')[7])
print("...DONE")


'''
	join starts and stops of each sequence, 
	then append actual sequnce to an array based
	on the positions of the starts and stops 
'''
seqs = zip(starts, stops)
finSeqs = []
for strt, stp in seqs:
	finSeqs.append(data[int(strt):int(stp)+1])


# combine the loci lables and sequences corrresponding to those labels
labeledSeqs = zip(loci, finSeqs)

# not needed anymore, may be useful for testing
'''
prints 1st 10 of the final paired loci-sequence combinations as a test
x = 0
for i in range(len(finSeqs)):
	if x == 10:
		break
	x+=1
	print(loci[i])
	print(textwrap.fill(finSeqs[i], 60))
'''


# create a list of every possible codon
codonCounts = {}
initCC = {}
everyCodonOut = []
nucleotides = "ACGT"
everyCodon = itertools.product(nucleotides, repeat = 3)
for i in everyCodon:
	everyCodonOut.append("".join(i)) #used for output at end
	codonCounts["".join(i)] = 0
	initCC["".join(i)] = 0


# go through each sequnce created and count the number of codon occurrences 
seqCodonCounts = []
print("GETTING CODON COUNTS...")
for i in range(len(finSeqs)):
	
	codonCountsLocal = defaultdict(lambda: 0, initCC)
		
	# test to make sure local is empty at this stage
	# for k,v in codonCountsLocal.items():
	# 	print(k,v)

	# "slide a window of string length 3" to count each occurence of a codon 
	for j in range(len(finSeqs[i])):
		if (j+1)%3 == 0 and finSeqs[i][j:j+3] in codonCounts.keys():
			codonCounts[finSeqs[i][j:j+3]] +=1
			codonCountsLocal[finSeqs[i][j:j+3]] +=1


	# create an array for holding the count dict contents as a list
	tmpCCL = []
	for key,value in codonCountsLocal.items():
		tmpCCL.append((key,value))

	seqCodonCounts.append((loci[i], tmpCCL))

print("...DONE")
'''
NEW ADDITION: 4/18/17
CUI CALCULATION
'''

pvalues = []
qvalues = []
CUIs = []

codons = []
for i in seqCodonCounts:
	codons.append(i[1])

# get L values
Lvalues = []
for i in range(len(finSeqs)):
	Lvalues.append(len(finSeqs[i])/3)
print(Lvalues[:10])

# get q values
for i in range(len(finSeqs)):
	qTEMP = []
	for j in range(len(codons[i])):
		qTEMP.append(float(codons[i][j][1])/float(Lvalues[i]))

	qvalues.append(qTEMP)

print(qvalues[:5])

# get tvalue
Tvalue = float(len(data)/3)
# print("tval: ", Tvalue)

# new codon dict
newCodonDict = {}
for i in everyCodonOut:
	if i in everyCodonOut:
		newCodonDict[i] = 0
for i in range(len(data)):
	if (i+1)%3 == 0 and data[i:i+3] in codonCounts.keys():
			newCodonDict[data[i:i+3]] +=1
# print(newCodonDict)

for key, value in newCodonDict.items():
	pvalues.append((key, float(value)/Tvalue))


# get final CUIs:
for i in range(len(qvalues)):
	CUIsOneSEQ = 0.0
	for j in range(len(qvalues[i])):
		CUIsOneSEQ += pvalues[j][1]*qvalues[i][j]

	CUIs.append((loci[i], CUIsOneSEQ))

print("CUIS")
print(CUIs[:10])

for entry in CUIs:
	print entry[0] + '\t' + str(entry[1])


'''
NEW ADDITION ENDS
'''



# separate into labels and sequences
sCCLabs = []
sCCSeqs = []
for i in seqCodonCounts:
	sCCLabs.append(i[0])
	sCCSeqs.append(i[1])

# separate the values back out using 2 transitional arrays 
sCCSNums = []
for i in sCCSeqs:
	sCCSNumsTEMP = []
	sCCSNumsTEMPNUMS = []
	sCCSNumsTEMP = i
	for j in range(len(sCCSNumsTEMP)): #append all numbers from temp to tempnums to get into array sccsnums
		sCCSNumsTEMPNUMS.append(sCCSNumsTEMP[j][1])

	sCCSNums.append(sCCSNumsTEMPNUMS)

# print("temp nums", sCCSNumsTEMPNUMS)
# print("temp: ", sCCSNumsTEMP)
# print("sCCSNums", sCCSNums[:5])

wfile = open("outputex3.txt", 'w')

wfile.write("        ")
for i in everyCodonOut:
	wfile.write(i + " ")
wfile.write("LENGTH")
wfile.write('\n')
for i in range(len(seqCodonCounts)):
	wfile.write('{}\t{}\t{}'.format(sCCLabs[i], sCCSNums[i], len(finSeqs[i])))
	wfile.write('\n')

wfile.close()





