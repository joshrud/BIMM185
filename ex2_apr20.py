"""
+
+	Josh Rudolph
+	BIMM185
+	ex1_apr20.py
+	extracts data from fasta files: '*.fa/*.fasta'
+
+
"""

from Bio import SeqIO
import sys

fasta_file = sys.argv[1]
    
print("accession", '\t', "sequence")
for record in SeqIO.parse(fasta_file, "fasta"):
    accession = record.id
    sequence = record.seq
    print accession, sequence








