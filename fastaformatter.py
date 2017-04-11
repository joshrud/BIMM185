"""
Josh Rudolph
BIMM185
4/6/17

"""

with open("TCDB.faa", "r") as rfile:

	headers = []
	protSeq = ""
	proteins = []

	x=0
	for line in rfile:
		if x==98:
			break
		if line[0] == '>':
			splitHeader = line.rstrip('\n').split('|')
			headers.append(splitHeader)
			if x == 0:
				continue
			proteins.append(protSeq)
			protSeq = ""

		else:
			protSeq += line.rstrip('\n')

		x+=1
	proteins.append(protSeq)

ID_2 = []
for i in headers:
	ID_2.append(i[2])
# print(ID_2)


ID_1 = []
for i in headers:
	curr = i[3].split(' ')
	currID = curr[0]
	ID_1.append(currID)

# print(ID_1)

# combine the two id's 
IDs = zip(ID_1, ID_2)



# print(IDs)



# print("proteins length: ", len(proteins))
# print("IDs length: ", len(IDs))
# print("LAST PROTEIN")
# print(proteins[-1])
# print("LAST ID")
# print(IDs[-1])



entries = []
for i in range(len(IDs)):
	currEntry = IDs[i][0] + " - " + IDs[i][1] + " - " + proteins[i]
	print(currEntry)
	entries.append(currEntry)





# print("FULL HEADERS:")
