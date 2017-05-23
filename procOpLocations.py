'''

Josh Rudolph
BIMM185
creates graphs for operon project: shows number of occurrences of distances between genes in and out of operons

'''





import sys
from scipy import stats
import matplotlib.pyplot as mpl
import numpy as np

# open file get data= genes and their locations 
with open(sys.argv[1], 'r') as rfile:
	data = []
	next(rfile)
	# gene_id exon    locus_tag       name    name    length  left_position   right_position  start   end     strand

	for line in rfile:
		data.append(line.rstrip('\n').split('\t'))


print("length: ",len(data))
# initialize some values to use later
prevOp = ""
prevRight = 0
prevLeft = 0
right = 0
left = 0
prevDirection = "reverse"
h0 = []
h1 = []
# sort the data
sorted_data = sorted( data, key=lambda x: int(x[0]) )

# go through each gene and get negative and positive control values
for x in sorted_data:

	print(x)
	# linedata = line.split('\t')
	left = int(x[6])
	right = int(x[7])

	# filter for multi-gene operons get positive control
	if x[4] == prevOp and prevDirection==x[-1]:

		distGene = left - prevRight + 1
		h1.append(distGene)

	# if the operon is different from the previous one, calculate the distance and append to h0 (negative control)
	if x[4] != prevOp and prevDirection==x[-1] :

		distOp = left - prevRight + 1
		h0.append(distOp)

	# take data to save as previous line data
	prevOp = x[4]
	prevRight = int(x[7])
	prevLeft = int(x[6])
	prevDirection = x[-1]


h0_processed = []
print(h1)
for i in range(len(h0)):
	if h0[i] < 1000:
		h0_processed.append(h0[i])

print(h0)
print(h0_processed)

xs = np.linspace(-100,3000,200)

kernel_h1 = stats.gaussian_kde(h1)
kernel_h1.covariance_factor = lambda:1.0
kernel_h1._compute_covariance()

# kernel_h0 = stats.gaussian_kde(h1)
# kernel_h0.covariance_factor = lambda:1.0
# kernel_h0._compute_covariance()


mpl.plot(xs, kernel_h1(xs))
# mpl.plot(xs, kernel_h0(xs))
mpl.show()





