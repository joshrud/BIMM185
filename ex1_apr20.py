"""
+
+	Josh Rudolph
+	BIMM185
+	ex1_apr20.py
+	extracts data from genbank files: '*.gbff'
+   program usage:    >python ex1_apr20.py <file.gbff> > <output file>
+
"""


from Bio import SeqIO #import Biopython libraries
import sys  #for taking command-line arguments


genbank_file = sys.argv[1] #parse input file
    
print "taxID", '\t',"accession", '\t', "coordinates", '\t', "strand", '\t', "gene name",'\t', "locus_tag",'\t', "gene_synonym",'\t', "protein name",'\t', "tax ID",'\t', "EC #",'\t', "external refs"      #title 
wanted = ["murE"] # or load all your 100 genes from a file
for record in SeqIO.parse(genbank_file, "genbank"):
    for f in record.features:
        # get taxID since not within CDS
    	if f.type == "source":
    		taxID = f.qualifiers["db_xref"][0].split(':')[1]

        # look for everything within CDS region
        if f.type == "CDS" and "gene" in f.qualifiers:
        	accession = "pseudo" #initialize the accession name 
        	protein_name = "pseudo" #initialize the protein name

            # check if the gene is a protein 
        	if "protein_id" in f.qualifiers:
        		accession = f.qualifiers["protein_id"]
        		protein_name = f.qualifiers["product"]
            # check if the gene is an enzyme
        	ecNum = "NO EC#"
        	if "EC_number" in f.qualifiers:
        		ecNum = f.qualifiers["EC_number"]

            # assign variables from data in gbff file
   	    	coordinates = [f.location.start, f.location.end]
	    	tempstrand = f.strand
            # determine if forward(+) or reverse(-) strand
	    	if str(tempstrand) == '1':
	    		strand = '+'
	    	else:
	    		strand = '-'

            # get last few variables
	    	gene = f.qualifiers["gene"]
	    	locusTag = f.qualifiers["locus_tag"]
	    	geneSyn = f.qualifiers["gene_synonym"]
	    	externalRefs = f.qualifiers["db_xref"]

        # print in loop: all variables just created
		print taxID, accession, coordinates, strand, gene, locusTag, geneSyn, protein_name, ecNum, externalRefs








