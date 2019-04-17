#! /usr/bin/env python3

from Bio import SeqIO
import argparse
import csv

# 1 create an argument parser object
parser = argparse.ArgumentParser(description="generate features given the start and end of a gene")

# positional argument
parser.add_argument( "start", type=str, help="start of a gene")
parser.add_argument( "end", type=str, help="end of a gene")

# optional  arguments
#add_argument("-c", "--CDS", action="store_true", help="print coding regions")
#add_argument("-s", "--strand", action="store_true", help="print positive strand")

# parse the arguments
args=parser.parse_args()

with open('watermelon.gff', 'r') as gff_file:
        csvreader = csv.reader(gff_file, delimiter='\t')
        for line in csvreader:
                if not line:
                        continue
                else:
                        if line[3] == args.start and line[4] ==  args.end:
                                print(line)


                                with open('watermelon.fsa', 'r') as fasta_file:
                                        for record in SeqIO.parse(fasta_file, 'fasta'):
                                                seq_whole = record.seq
                                                start = int(args.start) - 1
                                                end = int(args.end)
                                                seq_gene = seq_whole[start:end]
                                                length = len(seq_gene)
                                                print("The sequence of the gene from position " + args.start +  " to " + args.end +  " is " + "\n" + seq_gene)
                                                print("The length of the sequence is ",length)
                                                f_G = seq_gene.count('G')
                                                f_C = seq_gene.count('C')
                                                GC_content = (f_G + f_C)/length
                                                print("The GC content is ", GC_content)
                                                rev_com = seq_gene.reverse_complement()
                                                print("The reverse complement of the gene is " + "\n" + rev_com)

