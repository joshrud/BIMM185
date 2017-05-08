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



# COUNTERS
cntCDS = 4319   #4319 for a. tumefaciens
gnmCDS = 0
cntGenome = 1 
cntReplicons = 2 #2 for a tumefaciens
num_exons = 0
CDSlength = 0
geneName=""
locusTag=""
strand=""
protein_product=""
num_exons=0

genbank_file = sys.argv[1] #parse input file

for record in SeqIO.parse(genbank_file, "genbank"):
    
    if "complete genome" in record.description:
        replicon = "Chromosome"
    else:
        replicon = "Plasmid"

    accession = record.annotations["accessions"][0] #get accession #    
    release_date = record.annotations["date"]       #get release date
    structure = record.annotations["topology"]      #get replicon (linear/circular)
    domain = record.annotations["taxonomy"][0]      #get domain
    gnmSize = len(record)
    assembly = record.dbxrefs[-1].split(':')[1]

    for f in record.features:

        # get source information
    	if f.type == "source":
            taxID = f.qualifiers["db_xref"][0].split(':')[1]
            genome_name = "".join(f.qualifiers["organism"])
            if "Coli" in genome_name:
                cntGenome=1
            elif "tumefacien" in genome_name:
                cntGenome=2

        # CDS information
        if f.type == "CDS" and "gene" in f.qualifiers:

            cntCDS+=1 #iterate genbank file counter
            gnmCDS+=1 #iterate genome counter

            # assign variables from data in gbff file
            coordStart = f.location.start 
            coordEnd = f.location.end
            coordinates = str(coordStart) + "," + str(coordEnd)
            length = coordEnd - coordStart + 1
            size_bp=str(length)
            tempstrand = f.strand
            locusTag = f.qualifiers.get('locus_tag')[0]
            
            if "gene" in f.qualifiers:
                geneName = f.qualifiers["gene"][0]
            else:
                geneName = locusTag

            # determine if forward(+) or reverse(-) strand
            if str(tempstrand) == '1':
                strand = 'F'
            else:
                strand = 'R'

            num_exons = len(f.location.parts)
            CDSlength = 0
            num_exons = 0
            for exon in f.location.parts:
                num_exons +=1
                # print exon entry
                print "INSERT INTO exons (gene_id, exon, left_position, right_position, length) VALUES ("+str(cntCDS)+','+str(num_exons)+','+str(exon.start)+','+str(exon.end)+','+str(exon.end-exon.start+1)+");" 
                CDSlength+=exon.end-exon.start+1

            # provide default strings for accession and protein_name
            protID = "pseudo" #initialize the accession name 
            protein_product = "pseudo" #initialize the protein name

            # check if the gene is a protein 
            if "protein_id" in f.qualifiers:
                protID = "".join(f.qualifiers["protein_id"])
                protein_product =  "".join(f.qualifiers["product"])

        
            print "INSERT INTO genes (gene_id, genome_id, replicon_id, locus_tag, protein_id, name, strand, num_exons, length, product) VALUES ("+str(cntCDS)+','+str(cntGenome)+','+str(cntReplicons)+',\''+locusTag+'\',\''+protID+'\',\''+geneName+'\',\''+strand+'\','+str(num_exons)+','+str(CDSlength)+',\"'+protein_product+'\"'+");" 


        # GENOME INFO: GENOME_ID=$cntGenome, NAME=$genome_name, TAX_ID=$tax_id, domain=$domain, num_replicons=$cntReplicons, num_genes=$gnmCDS, size_bp=$gnmSize, assembly=$assembly 
        # REPLICONS INFO: replicon_id=$cntReplicons, genome_id=$cntGenome, name, type(chrom/plasm), shape(lin/circ), num_genes, size_bp, accession, release_date
        # GENES INFO: gene_id, genome_id, replicon_id, locus_tag, protein_id, name, strand, num_exons, length, product
        # EXON INFO: g


    # print genome and replicon entries
     
    print "INSERT INTO replicons (replicon_id, genome_id, name, type, shape, num_genes, size_bp, accession, release_date) VALUES ("+str(cntReplicons)+','+str(cntGenome)+',\''+genome_name+'\',\''+replicon+'\',\''+structure+'\','+str(gnmCDS)+','+str(gnmSize)+',\''+accession+'\',\''+release_date+'\''+");" 

    cntReplicons +=1 #iterate replicon number 

print "INSERT INTO genomes (genome_id, name, tax_id, domain, num_replicons, num_genes, size_bp, assembly) VALUES ("+str(cntGenome)+',\''+genome_name+'\','+str(taxID)+',\''+ domain + '\','+str(cntReplicons)+','+str(gnmCDS)+','+str(gnmSize)+',\''+assembly+'\''+");"

# get last few variables
# genome_id = "genome_id"
# replicon_id = "replicon_id"

# gene = "".join(f.qualifiers["gene"])
# name_short =gene
# locusTag = "".join(f.qualifiers["locus_tag"])
# geneSyn = "".join(f.qualifiers["gene_synonym"])
# externalRefs = "".join(f.qualifiers["db_xref"])



# check if the gene is an enzyme
# ecNum = "NO EC#"
# if "EC_number" in f.qualifiers:
#     ecNum = f.qualifiers["EC_number"]



