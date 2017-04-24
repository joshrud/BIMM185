"""
+
+	Josh Rudolph
+	BIMM185
+	ex1_apr20.py
+	extracts data from genbank files: '*.gbff'
+
+
"""

from Bio import SeqIO
import sys

genbank_file = sys.argv[1]
    
print "taxID", '\t',"accession", '\t', "coordinates", '\t', "strand", '\t', "gene name",'\t', "locus_tag",'\t', "gene_synonym",'\t', "protein name",'\t', "tax ID",'\t', "EC #",'\t', "external refs"      #title 
wanted = ["murE"] # or load all your 100 genes from a file
for record in SeqIO.parse(genbank_file, "genbank"):
    for f in record.features:
    	if f.type == "source":
    		taxID = f.qualifiers["db_xref"][0].split(':')[1]
        if f.type == "CDS" and "gene" in f.qualifiers:
        	accession = "pseudo"
        	protein_name = "pseudo"
        	if "protein_id" in f.qualifiers:
        		accession = f.qualifiers["protein_id"]
        		protein_name = f.qualifiers["product"]
        	ecNum = "NO EC#"
        	if "EC_number" in f.qualifiers:
        		ecNum = f.qualifiers["EC_number"]
   	    	coordinates = [f.location.start, f.location.end]
	    	tempstrand = f.strand
	    	if str(tempstrand) == '1':
	    		strand = '+'
	    	else:
	    		strand = '-'
	    	gene = f.qualifiers["gene"]
	    	locusTag = f.qualifiers["locus_tag"]
	    	geneSyn = f.qualifiers["gene_synonym"]
	    	externalRefs = f.qualifiers["db_xref"]
		print taxID, accession, coordinates, strand, gene, locusTag, geneSyn, protein_name, ecNum, externalRefs








