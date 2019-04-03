#! /usr/bin/env python3


import argparse
#create an ArgumentParser object('parser') that will hold all the information necessary to parse the command line
parser = argparse.ArgumentParser(description = "generates the features of a particular gene")

#add arguments
parser.add_argument( "gene_name", help="name of the job" )
parser.add_argument( "type", help="tRNA, CDS, Intron, MF" )
parser.add_argument( "begin", help="beginning of the gene" )
parser.add_argument( "end", help="end of the gene" )
parser.add_argument( "length", help="length of the gene" )
parser.add_argument( "strand", help="strand of the gene" )
parser.add_argument( "features", help="features of the gene" )     

#add optional arguments -- makes it optional
#parser.add_argument( "-q", "--queue", help="name of the Trestles queue (default=06h32c", default="q06h32c")
#parser.add_argument( "-p", "--ppn", help="number of processors (default=32)", type=int, default=32)
#parser.add_argument( "-w", "--walltime", help="amount needed for the job (default=6)", type=int, default=6)

#parse the command line arguments
args = parser.parse_args()

print("Gene Name:", args.gene_name)
print("Type:", args.type)
print("Begin:", args.begin)
print("End:", args.end)
print("Length:", args.length)
print("Strand:", args.strand)
print("Features:", args.features)

