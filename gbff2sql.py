"""
+
+	Josh Rudolph
+	BIMM185
+	extracts data from genbank files: '*.gbff'
+   program usage:    >python gbff2sql.py <file.gbff> > <output file>
+
"""


from Bio import SeqIO #import Biopython libraries
import sys  #for taking command-line arguments
genome_id = "genome_id"
replicon_id = "replicon_id"
gene = "gene"
locusTag = "tag"
geneSyn = "syn"
externalRefs = "ref"
protein_name = "prot"
length = 0
accession = "accession"
name_short="name_short"
name_long = "name_long"
size_bp="size_bp"
domain="bacteria"

genbank_file = sys.argv[1] #parse input file
    
# print "taxID", '\t',"accession", '\t', "coordinates", '\t', "strand", '\t', "gene name",'\t', "locus_tag",'\t', "gene_synonym",'\t', "protein name",'\t', "tax ID",'\t', "EC #",'\t', "external refs"      #title 
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
            	accession = "".join(f.qualifiers["protein_id"])
            	protein_name =  "".join(f.qualifiers["product"])
                name_long=protein_name
                name_long.replace('"','')
                name_long.replace("'",'')
            # check if the gene is an enzyme
            ecNum = "NO EC#"
            if "EC_number" in f.qualifiers:
                ecNum = f.qualifiers["EC_number"]

            # assign variables from data in gbff file
            coordStart = f.location.start 
            coordEnd = f.location.end
            coordinates = str(coordStart) + "," + str(coordEnd)
            length = coordEnd - coordStart + 1
            size_bp=str(length)
            tempstrand = f.strand
            # determine if forward(+) or reverse(-) strand
            if str(tempstrand) == '1':
                strand = '+'
            else:
                strand = '-'

            # get last few variables
            genome_id = "genome_id"
            replicon_id = "replicon_id"
            gene = "".join(f.qualifiers["gene"])
            name_short =gene
            locusTag = "".join(f.qualifiers["locus_tag"])
            geneSyn = "".join(f.qualifiers["gene_synonym"])
            externalRefs = "".join(f.qualifiers["db_xref"])

        # print in loop: all variables just created

        print "INSERT INTO genomes (tax_id,name_short, size_bp, accession) VALUES ("+str(taxID)+',\''+name_short+'\','+size_bp+',\''+accession+'\''+");" 





        # taxID, '\t', gene, '\t',protein_name, '\t', length, '\t', "bacteria", '\t',  accession 

        # '\t', locusTag,  '\t', strand, '\t', exons, '\t' ,geneSyn 








