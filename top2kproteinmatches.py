"""
Josh Rudolph
BIMM185
4/6/17

"""
import bz2
import operator 

print("decompressing....")
uncompressedData = bz2.BZ2File("RS.txt.bz2").read()
print("...done")

# print(uncompressedData[:1000])

print("splitting into lines....")
lines = uncompressedData.split('\n')
print("...done")


# print("LINE1: ", lines[0])

print("splitting by tab chars...")
for i in range(len(lines)): 
	lines[i] = lines[i].split('\t')
print("...done")

# print("LINE1-10 FORMATTED: ", lines[:5])

topProteins = []
maxProteins = 20  #will be 2k
numProtein = 0
i=0



while numProtein <= maxProteins: 

	protMatches = {}
	currProt = lines[i][0]

	if i>0:
		
		j=0
		while currProt == lines[i+j-1][0]:
			protMatches[lines[i+j][1]] = lines[i+j][3]
			j+=1
		numProtein+=1
		best = [key for key, value in protMatches.iteritems() if value == max(protMatches.values())] 
		topProteins.append(best)
		# print(protMatches)
		# print("length: ", len(protMatches))



	i+=1

print(topProteins)


