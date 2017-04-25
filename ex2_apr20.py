"""
+
+	Josh Rudolph
+	BIMM185
+	ex2_apr20.py
+	extracts data from fasta files: '*.fa/*.fasta'
+	program usage:    >python ex2_apr20.py <file.fasta> > <output file>
+
"""

from Bio import SeqIO #get biopython libraries
import sys	#for getting commandline arguments

fasta_file = sys.argv[1] #parse input file
   

print("accession", '\t', "sequence")
# go through each sequence in the fasta file
for record in SeqIO.parse(fasta_file, "fasta"):
	# save some variables
    accession = record.id
    sequence = record.seq
    print accession, sequence








