

```python
import os
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
```

    reading sequences from xaj.dna
    reading sequences from xah.dna
    reading sequences from xai.dna
    reading sequences from xaf.dna
    reading sequences from xag.dna
    reading sequences from xae.dna
    reading sequences from xad.dna
    reading sequences from xac.dna
    reading sequences from xab.dna
    reading sequences from xaa.dna



```python
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        dna_file = open(file_name)
        # look at each line
        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            print("found a dna sequence with length " + str(length))
```

    reading sequences from xaj.dna
    found a dna sequence with length 121
    found a dna sequence with length 442
    found a dna sequence with length 520
    found a dna sequence with length 866
    found a dna sequence with length 969
    found a dna sequence with length 672
    found a dna sequence with length 138
    found a dna sequence with length 922
    found a dna sequence with length 652
    found a dna sequence with length 749
    reading sequences from xah.dna
    found a dna sequence with length 575
    found a dna sequence with length 987
    found a dna sequence with length 141
    found a dna sequence with length 590
    found a dna sequence with length 833
    found a dna sequence with length 200
    found a dna sequence with length 539
    found a dna sequence with length 625
    found a dna sequence with length 363
    found a dna sequence with length 779
    reading sequences from xai.dna
    found a dna sequence with length 317
    found a dna sequence with length 382
    found a dna sequence with length 324
    found a dna sequence with length 747
    found a dna sequence with length 353
    found a dna sequence with length 878
    found a dna sequence with length 692
    found a dna sequence with length 806
    found a dna sequence with length 118
    found a dna sequence with length 556
    reading sequences from xaf.dna
    found a dna sequence with length 242
    found a dna sequence with length 714
    found a dna sequence with length 291
    found a dna sequence with length 313
    found a dna sequence with length 926
    found a dna sequence with length 738
    found a dna sequence with length 516
    found a dna sequence with length 218
    found a dna sequence with length 558
    found a dna sequence with length 465
    reading sequences from xag.dna
    found a dna sequence with length 432
    found a dna sequence with length 818
    found a dna sequence with length 604
    found a dna sequence with length 879
    found a dna sequence with length 619
    found a dna sequence with length 500
    found a dna sequence with length 119
    found a dna sequence with length 341
    found a dna sequence with length 303
    found a dna sequence with length 469
    reading sequences from xae.dna
    found a dna sequence with length 600
    found a dna sequence with length 707
    found a dna sequence with length 853
    found a dna sequence with length 971
    found a dna sequence with length 279
    found a dna sequence with length 533
    found a dna sequence with length 452
    found a dna sequence with length 332
    found a dna sequence with length 990
    found a dna sequence with length 899
    reading sequences from xad.dna
    found a dna sequence with length 949
    found a dna sequence with length 453
    found a dna sequence with length 988
    found a dna sequence with length 420
    found a dna sequence with length 767
    found a dna sequence with length 221
    found a dna sequence with length 316
    found a dna sequence with length 573
    found a dna sequence with length 231
    found a dna sequence with length 409
    reading sequences from xac.dna
    found a dna sequence with length 665
    found a dna sequence with length 165
    found a dna sequence with length 677
    found a dna sequence with length 454
    found a dna sequence with length 426
    found a dna sequence with length 600
    found a dna sequence with length 177
    found a dna sequence with length 888
    found a dna sequence with length 535
    found a dna sequence with length 974
    reading sequences from xab.dna
    found a dna sequence with length 833
    found a dna sequence with length 390
    found a dna sequence with length 355
    found a dna sequence with length 968
    found a dna sequence with length 999
    found a dna sequence with length 257
    found a dna sequence with length 909
    found a dna sequence with length 236
    found a dna sequence with length 943
    found a dna sequence with length 703
    reading sequences from xaa.dna
    found a dna sequence with length 333
    found a dna sequence with length 283
    found a dna sequence with length 380
    found a dna sequence with length 115
    found a dna sequence with length 753
    found a dna sequence with length 764
    found a dna sequence with length 234
    found a dna sequence with length 117
    found a dna sequence with length 906
    found a dna sequence with length 160



```python
# go through each file in the folder
for file_name in os.listdir("."):
  # check if it ends with .dna
  if file_name.endswith(".dna"):
    print("reading sequences from " + file_name)
    # open the file and process each line
    dna_file = open(file_name)
    for line in dna_file:
      # calculate the sequence length
      dna = line.rstrip("\n")
      length = len(dna)
      print("sequence length is " + str(length))
      # go through each bin and check if the sequence belongs in it
      for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
          print("bin is " + str(bin_lower) + " to " + str(bin_upper))
```

    reading sequences from xaj.dna
    sequence length is 121
    bin is 100 to 199
    sequence length is 442
    bin is 400 to 499
    sequence length is 520
    bin is 500 to 599
    sequence length is 866
    bin is 800 to 899
    sequence length is 969
    bin is 900 to 999
    sequence length is 672
    bin is 600 to 699
    sequence length is 138
    bin is 100 to 199
    sequence length is 922
    bin is 900 to 999
    sequence length is 652
    bin is 600 to 699
    sequence length is 749
    bin is 700 to 799
    reading sequences from xah.dna
    sequence length is 575
    bin is 500 to 599
    sequence length is 987
    bin is 900 to 999
    sequence length is 141
    bin is 100 to 199
    sequence length is 590
    bin is 500 to 599
    sequence length is 833
    bin is 800 to 899
    sequence length is 200
    bin is 200 to 299
    sequence length is 539
    bin is 500 to 599
    sequence length is 625
    bin is 600 to 699
    sequence length is 363
    bin is 300 to 399
    sequence length is 779
    bin is 700 to 799
    reading sequences from xai.dna
    sequence length is 317
    bin is 300 to 399
    sequence length is 382
    bin is 300 to 399
    sequence length is 324
    bin is 300 to 399
    sequence length is 747
    bin is 700 to 799
    sequence length is 353
    bin is 300 to 399
    sequence length is 878
    bin is 800 to 899
    sequence length is 692
    bin is 600 to 699
    sequence length is 806
    bin is 800 to 899
    sequence length is 118
    bin is 100 to 199
    sequence length is 556
    bin is 500 to 599
    reading sequences from xaf.dna
    sequence length is 242
    bin is 200 to 299
    sequence length is 714
    bin is 700 to 799
    sequence length is 291
    bin is 200 to 299
    sequence length is 313
    bin is 300 to 399
    sequence length is 926
    bin is 900 to 999
    sequence length is 738
    bin is 700 to 799
    sequence length is 516
    bin is 500 to 599
    sequence length is 218
    bin is 200 to 299
    sequence length is 558
    bin is 500 to 599
    sequence length is 465
    bin is 400 to 499
    reading sequences from xag.dna
    sequence length is 432
    bin is 400 to 499
    sequence length is 818
    bin is 800 to 899
    sequence length is 604
    bin is 600 to 699
    sequence length is 879
    bin is 800 to 899
    sequence length is 619
    bin is 600 to 699
    sequence length is 500
    bin is 500 to 599
    sequence length is 119
    bin is 100 to 199
    sequence length is 341
    bin is 300 to 399
    sequence length is 303
    bin is 300 to 399
    sequence length is 469
    bin is 400 to 499
    reading sequences from xae.dna
    sequence length is 600
    bin is 600 to 699
    sequence length is 707
    bin is 700 to 799
    sequence length is 853
    bin is 800 to 899
    sequence length is 971
    bin is 900 to 999
    sequence length is 279
    bin is 200 to 299
    sequence length is 533
    bin is 500 to 599
    sequence length is 452
    bin is 400 to 499
    sequence length is 332
    bin is 300 to 399
    sequence length is 990
    bin is 900 to 999
    sequence length is 899
    reading sequences from xad.dna
    sequence length is 949
    bin is 900 to 999
    sequence length is 453
    bin is 400 to 499
    sequence length is 988
    bin is 900 to 999
    sequence length is 420
    bin is 400 to 499
    sequence length is 767
    bin is 700 to 799
    sequence length is 221
    bin is 200 to 299
    sequence length is 316
    bin is 300 to 399
    sequence length is 573
    bin is 500 to 599
    sequence length is 231
    bin is 200 to 299
    sequence length is 409
    bin is 400 to 499
    reading sequences from xac.dna
    sequence length is 665
    bin is 600 to 699
    sequence length is 165
    bin is 100 to 199
    sequence length is 677
    bin is 600 to 699
    sequence length is 454
    bin is 400 to 499
    sequence length is 426
    bin is 400 to 499
    sequence length is 600
    bin is 600 to 699
    sequence length is 177
    bin is 100 to 199
    sequence length is 888
    bin is 800 to 899
    sequence length is 535
    bin is 500 to 599
    sequence length is 974
    bin is 900 to 999
    reading sequences from xab.dna
    sequence length is 833
    bin is 800 to 899
    sequence length is 390
    bin is 300 to 399
    sequence length is 355
    bin is 300 to 399
    sequence length is 968
    bin is 900 to 999
    sequence length is 999
    sequence length is 257
    bin is 200 to 299
    sequence length is 909
    bin is 900 to 999
    sequence length is 236
    bin is 200 to 299
    sequence length is 943
    bin is 900 to 999
    sequence length is 703
    bin is 700 to 799
    reading sequences from xaa.dna
    sequence length is 333
    bin is 300 to 399
    sequence length is 283
    bin is 200 to 299
    sequence length is 380
    bin is 300 to 399
    sequence length is 115
    bin is 100 to 199
    sequence length is 753
    bin is 700 to 799
    sequence length is 764
    bin is 700 to 799
    sequence length is 234
    bin is 200 to 299
    sequence length is 117
    bin is 100 to 199
    sequence length is 906
    bin is 900 to 999
    sequence length is 160
    bin is 100 to 199



```python
for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
    os.mkdir(bin_folder_name)
```


```python
test_dna = "ACTGTAGCTGTACGTAGC"
print(test_dna)
kmer_size = 4
for start in range(0,len(test_dna)-(kmer_size-1),1):
    kmer = test_dna[start:start+kmer_size]
    print(kmer)
```

    ACTGTAGCTGTACGTAGC
    ACTG
    CTGT
    TGTA
    GTAG
    TAGC
    AGCT
    GCTG
    CTGT
    TGTA
    GTAC
    TACG
    ACGT
    CGTA
    GTAG
    TAGC



```python
def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers
print(split_dna("AATGCTGCAT", 4))
print(split_dna("AATGCTGCAT", 5))
print(split_dna("AATGCTGCAT", 6))
```

    ['AATG', 'ATGC', 'TGCT', 'GCTG', 'CTGC', 'TGCA', 'GCAT']
    ['AATGC', 'ATGCT', 'TGCTG', 'GCTGC', 'CTGCA', 'TGCAT']
    ['AATGCT', 'ATGCTG', 'TGCTGC', 'GCTGCA', 'CTGCAT']



```python
import os
kmer_size = 6

def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

kmer_counts = {}
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        dna_file = open(file_name)
        for line in dna_file:
            dna= line.rstrip("\n")
            for kmer in split_dna(dna, kmer_size):
                current_count = kmer_counts.get(kmer, 0)
                new_count = current_count + 1
                kmer_counts[kmer] = new_count
                    
print(kmer_counts)
```

    reading sequences from xaj.dna
    reading sequences from xah.dna
    reading sequences from xai.dna
    reading sequences from xaf.dna
    reading sequences from xag.dna
    reading sequences from xae.dna
    reading sequences from xad.dna
    reading sequences from xac.dna
    reading sequences from xab.dna
    reading sequences from xaa.dna
    {'aattat': 12, 'attatt': 12, 'ttattc': 11, 'tattca': 16, 'attcac': 22, 'ttcact': 19, 'tcactg': 13, 'cactgc': 18, 'actgca': 15, 'ctgcat': 11, 'tgcata': 14, 'gcatag': 13, 'catagt': 11, 'atagtt': 15, 'tagtta': 7, 'agttag': 9, 'gttaga': 23, 'ttagac': 17, 'tagacc': 10, 'agaccg': 12, 'gaccgc': 11, 'accgct': 16, 'ccgctg': 7, 'cgctgc': 8, 'gctgcg': 8, 'ctgcgt': 7, 'tgcgta': 14, 'gcgtag': 9, 'cgtagc': 12, 'gtagcc': 23, 'tagcct': 16, 'agcctc': 12, 'gcctca': 16, 'cctcaa': 13, 'ctcaat': 11, 'tcaatc': 11, 'caatcg': 11, 'aatcgg': 15, 'atcggt': 9, 'tcggtt': 13, 'cggttg': 17, 'ggttgt': 13, 'gttgtg': 12, 'ttgtgc': 11, 'tgtgcc': 11, 'gtgcct': 6, 'tgcctt': 15, 'gccttc': 21, 'ccttca': 20, 'cttcac': 18, 'cactga': 17, 'actgac': 12, 'ctgacg': 12, 'tgacgt': 12, 'gacgtt': 15, 'acgttt': 17, 'cgtttg': 11, 'gtttga': 13, 'tttgaa': 7, 'ttgaaa': 14, 'tgaaag': 14, 'gaaagc': 16, 'aaagca': 18, 'aagcac': 14, 'agcacg': 8, 'gcacgt': 7, 'cacgtt': 12, 'acgttc': 18, 'cgttca': 14, 'gttcac': 18, 'ttcacg': 23, 'tcacga': 17, 'cacgaa': 19, 'acgaac': 13, 'cgaact': 10, 'gaactt': 12, 'aactta': 13, 'acttac': 18, 'cttacc': 15, 'ttaccc': 8, 'taccca': 18, 'acccat': 14, 'cccatg': 12, 'ccatga': 12, 'catgag': 12, 'atgagg': 12, 'tgagga': 17, 'gaggaa': 12, 'aggaag': 9, 'ggaagt': 4, 'gaagta': 6, 'aagtag': 13, 'agtagc': 12, 'gtagca': 14, 'tagcat': 17, 'agcatg': 13, 'gcatgg': 17, 'catggc': 16, 'atggcg': 13, 'tggcgt': 12, 'ggcgtc': 10, 'gcgtcc': 9, 'cgtcct': 8, 'gtcctg': 15, 'tcctga': 19, 'cctgag': 19, 'ctgaga': 18, 'tgagag': 17, 'gagagc': 17, 'agagcg': 13, 'gagcgg': 12, 'agcggc': 8, 'gcggct': 9, 'cggcta': 17, 'agtatc': 13, 'gtatca': 15, 'tatcac': 9, 'atcacc': 9, 'tcaccc': 16, 'caccca': 16, 'acccag': 14, 'cccagc': 24, 'ccagcc': 14, 'cagccc': 15, 'agccct': 16, 'gcccta': 17, 'ccctag': 13, 'cctagt': 10, 'ctagtc': 15, 'tagtcc': 11, 'agtccg': 17, 'gtccga': 11, 'tccgaa': 14, 'ccgaat': 14, 'cgaatt': 21, 'gaattc': 20, 'aattcc': 9, 'attccg': 18, 'ttccgc': 17, 'tccgcg': 11, 'ccgcgt': 7, 'cgcgtg': 12, 'gcgtgt': 15, 'cgtgta': 11, 'gtgtac': 21, 'tgtacc': 17, 'gtacca': 14, 'taccaa': 18, 'accaag': 13, 'ccaagt': 18, 'caagtt': 15, 'aagtta': 11, 'agttaa': 16, 'gttaac': 21, 'ttaacc': 17, 'taacct': 21, 'aacctc': 17, 'acctct': 20, 'cctctg': 14, 'ctctgg': 13, 'tctgga': 21, 'ctggag': 12, 'tggaga': 15, 'ggagaa': 16, 'gagaac': 16, 'agaacc': 11, 'gaaccg': 21, 'aaccgg': 22, 'accggt': 18, 'ccggtt': 26, 'cggtta': 18, 'ggttag': 22, 'gttagt': 8, 'ttagta': 11, 'tagtac': 10, 'agtacc': 10, 'gtaccg': 16, 'taccga': 14, 'accgag': 18, 'ccgagg': 15, 'cgagga': 12, 'gaggat': 12, 'aggatg': 13, 'ggatgg': 15, 'gatggc': 15, 'atggct': 24, 'tggcta': 22, 'ggctaa': 11, 'gctaag': 12, 'ctaaga': 14, 'taagag': 13, 'aagagc': 16, 'gagcga': 20, 'agcgaa': 15, 'gcgaag': 14, 'cgaagt': 12, 'gaagtg': 5, 'aagtga': 12, 'agtgat': 16, 'gtgatc': 16, 'tgatcc': 11, 'gatccc': 21, 'atccct': 18, 'tccctc': 16, 'ccctca': 10, 'cctcat': 14, 'ctcata': 17, 'tcatat': 12, 'catata': 17, 'atatat': 12, 'tatata': 7, 'tatatt': 14, 'atattg': 18, 'tattgc': 16, 'attgcc': 20, 'ttgccc': 15, 'tgccct': 12, 'gccctc': 19, 'ccctcc': 19, 'cctcct': 13, 'ctccta': 18, 'tcctat': 18, 'cctatc': 9, 'ctatca': 10, 'atcacg': 16, 'tcacgg': 17, 'cacggt': 16, 'acggtg': 17, 'cggtgg': 9, 'ggtggg': 14, 'gtgggg': 11, 'tgggga': 10, 'ggggag': 7, 'gggagt': 7, 'ggagtc': 10, 'gagtcg': 9, 'agtcgg': 13, 'gtcggg': 10, 'tcggga': 14, 'cgggat': 12, 'gggatt': 15, 'ggattc': 19, 'gattct': 16, 'attctg': 17, 'ttctga': 26, 'tctgac': 12, 'tgacga': 9, 'gacgag': 13, 'acgagt': 15, 'cgagta': 11, 'gagtaa': 5, 'agtaaa': 12, 'gtaaag': 14, 'taaagt': 16, 'aaagtg': 10, 'aagtgg': 20, 'agtggc': 21, 'gtggct': 14, 'gctaat': 15, 'ctaatc': 13, 'taatca': 15, 'aatcat': 12, 'atcata': 11, 'tcatag': 9, 'atagtc': 13, 'tagtcg': 12, 'agtcgt': 7, 'gtcgtt': 10, 'tcgtta': 15, 'cgttaa': 22, 'taaccg': 16, 'ggttgc': 23, 'gttgcc': 15, 'ttgcct': 16, 'gccttg': 11, 'ccttga': 8, 'cttgat': 10, 'ttgatg': 18, 'tgatga': 12, 'gatgaa': 15, 'atgaac': 14, 'tgaaca': 11, 'gaacat': 19, 'aacatg': 15, 'acatgt': 18, 'catgta': 20, 'atgtac': 9, 'taccag': 14, 'accaga': 8, 'ccagag': 11, 'cagagg': 21, 'agaggc': 19, 'gaggca': 21, 'aggcat': 12, 'ggcatc': 20, 'gcatcg': 20, 'catcga': 19, 'atcgaa': 16, 'tcgaag': 9, 'gaagtt': 10, 'aagttt': 12, 'agtttg': 13, 'gtttgt': 16, 'tttgtc': 11, 'ttgtcg': 14, 'tgtcga': 18, 'gtcgag': 19, 'tcgaga': 12, 'cgagaa': 9, 'gaaccc': 11, 'aacccg': 18, 'acccgt': 14, 'cccgtg': 14, 'ccgtgg': 12, 'cgtggg': 12, 'gtgggt': 11, 'tgggtg': 11, 'gggtgg': 11, 'gtgggc': 9, 'tgggcc': 12, 'gggcca': 14, 'ggccac': 11, 'gccact': 17, 'ccactg': 19, 'cactgt': 12, 'actgta': 10, 'ctgtat': 13, 'tgtatc': 17, 'gtatct': 20, 'tatctc': 22, 'atctct': 11, 'tctctt': 11, 'ctcttg': 13, 'tcttgg': 19, 'cttgga': 14, 'ttggac': 14, 'tggacc': 12, 'ggaccg': 16, 'gaccgt': 17, 'accgta': 21, 'ccgtac': 12, 'cgtacc': 15, 'gtaccc': 8, 'taccct': 11, 'accctc': 10, 'cctcag': 11, 'ctcagt': 7, 'tcagtt': 15, 'cagtta': 8, 'agttat': 14, 'gttata': 13, 'ttatag': 15, 'tatagt': 20, 'tagtct': 13, 'agtctt': 18, 'gtcttc': 14, 'tcttcc': 16, 'cttcca': 20, 'ttccag': 12, 'tccaga': 12, 'ccagat': 12, 'cagatt': 14, 'agattt': 9, 'gatttc': 14, 'atttct': 16, 'tttctc': 12, 'ttctca': 19, 'tctcag': 8, 'tcagtg': 11, 'cagtga': 15, 'agtgag': 11, 'gtgagt': 11, 'tgagtc': 20, 'gagtcc': 13, 'agtcca': 8, 'gtccag': 15, 'ccagac': 9, 'cagaca': 12, 'agacag': 12, 'gacaga': 15, 'acagat': 20, 'cagata': 16, 'agatat': 15, 'gatatc': 21, 'atatcc': 13, 'tatccc': 15, 'atcccg': 15, 'tcccgc': 17, 'cccgcg': 16, 'ccgcgc': 15, 'cgcgcg': 15, 'gcgcgt': 11, 'cgcgtt': 15, 'gcgtta': 16, 'cgttag': 18, 'ttagag': 15, 'tagagg': 13, 'gaggct': 11, 'aggctc': 18, 'ggctct': 14, 'gctcta': 13, 'ctctac': 16, 'tctact': 14, 'ctacta': 13, 'tactac': 12, 'actaca': 9, 'ctacac': 19, 'tacaca': 17, 'acacag': 15, 'cacaga': 17, 'acagac': 12, 'cagacg': 18, 'agacgg': 15, 'gacggg': 17, 'acgggc': 14, 'cgggca': 12, 'gggcag': 12, 'ggcagt': 16, 'gcagtt': 16, 'cagttg': 21, 'agttgg': 12, 'gttgga': 12, 'ggacct': 9, 'gaccta': 12, 'acctag': 14, 'cctaga': 12, 'ctagac': 12, 'tagact': 12, 'agactg': 9, 'gactga': 13, 'actgaa': 16, 'ctgaac': 13, 'tgaacg': 19, 'gaacga': 6, 'aacgac': 11, 'acgaca': 17, 'cgacag': 12, 'gacagt': 10, 'acagtc': 7, 'cagtcg': 12, 'agtcgc': 10, 'gtcgct': 9, 'tcgcta': 12, 'cgctac': 20, 'gctacg': 14, 'ctacga': 9, 'tacgaa': 8, 'acgaat': 19, 'cgaata': 11, 'gaataa': 16, 'aataac': 21, 'ataacc': 18, 'aacctt': 14, 'accttg': 10, 'ccttgg': 14, 'cttggc': 17, 'ttggcc': 10, 'tggcct': 14, 'ggcctc': 16, 'gcctct': 15, 'ctctgt': 21, 'tctgtc': 13, 'ctgtcg': 15, 'tgtcgt': 10, 'gtcgtg': 7, 'tcgtgt': 11, 'cgtgtc': 19, 'gtgtct': 14, 'tgtctc': 11, 'gtctct': 18, 'tctctg': 15, 'ctctga': 7, 'tctgaa': 24, 'tgaact': 9, 'aacttt': 13, 'actttt': 12, 'cttttc': 10, 'ttttct': 11, 'tttctg': 16, 'gaacta': 7, 'aactaa': 15, 'actaaa': 10, 'ctaaat': 8, 'taaatg': 11, 'aaatgt': 12, 'aatgtc': 16, 'atgtct': 12, 'tgtctt': 18, 'gtcttt': 13, 'tctttt': 13, 'cttttg': 13, 'ttttgg': 14, 'tttgga': 15, 'ttggaa': 13, 'tggaat': 18, 'ggaatc': 19, 'gaatcc': 12, 'aatcca': 17, 'atccag': 18, 'cagaga': 8, 'agagac': 12, 'gagaca': 12, 'gacagc': 14, 'acagcc': 11, 'cagcca': 15, 'agccaa': 16, 'gccaag': 20, 'ccaagg': 15, 'caaggc': 19, 'aaggca': 18, 'aggcaa': 14, 'ggcaat': 15, 'caattt': 11, 'aatttc': 11, 'ttctcc': 18, 'tctccc': 14, 'ctccct': 12, 'cctccg': 12, 'ctccgg': 14, 'tccggc': 10, 'ccggca': 18, 'cggcaa': 13, 'gcaata': 13, 'caatag': 12, 'aatagc': 16, 'atagcg': 14, 'tagcgg': 13, 'agcggg': 26, 'gcggga': 18, 'cgggaa': 20, 'gggaag': 15, 'ggaaga': 13, 'gaagaa': 11, 'aagaaa': 14, 'agaaag': 15, 'gaaaga': 10, 'aaagag': 12, 'agagcc': 10, 'gagccc': 15, 'agcccc': 10, 'gccccc': 17, 'cccccg': 17, 'ccccga': 15, 'cccgag': 13, 'ccgagc': 12, 'cgagcg': 15, 'agcgat': 16, 'gcgatg': 16, 'cgatgc': 12, 'gatgct': 10, 'atgctg': 11, 'tgctgg': 16, 'gctggc': 12, 'ctggcg': 11, 'tggcgg': 13, 'ggcgga': 13, 'gcggag': 17, 'cggagt': 12, 'gagtct': 16, 'agtctg': 14, 'gtctgc': 16, 'tctgca': 20, 'ctgcac': 11, 'tgcacg': 11, 'gcacgg': 17, 'cacgga': 19, 'acggaa': 10, 'cggaaa': 23, 'ggaaat': 17, 'gaaatg': 11, 'aatgtg': 13, 'atgtgg': 9, 'tgtggc': 11, 'gtggca': 13, 'tggcac': 17, 'ggcact': 18, 'gcactg': 18, 'actgcg': 8, 'ctgcga': 11, 'tgcgac': 20, 'gcgacc': 13, 'cgacca': 13, 'gaccat': 19, 'accatc': 13, 'ccatcc': 5, 'catccg': 15, 'atccgc': 10, 'tccgcc': 14, 'ccgccc': 11, 'cgccct': 17, 'ccctcg': 10, 'cctcgg': 15, 'ctcgga': 14, 'tcggat': 15, 'cggata': 18, 'ggatag': 5, 'gatagg': 7, 'ataggg': 14, 'taggga': 12, 'agggat': 13, 'gggata': 8, 'ggataa': 19, 'gataaa': 10, 'ataaag': 10, 'agtgga': 17, 'gtggat': 17, 'tggatg': 21, 'ggatgt': 18, 'gatgtg': 14, 'atgtga': 14, 'tgtgat': 12, 'tgatcg': 13, 'gatcgt': 14, 'atcgtg': 17, 'tcgtga': 9, 'cgtgag': 17, 'gtgagg': 16, 'tgaggc': 19, 'ggcatg': 10, 'gcatga': 13, 'catgac': 13, 'atgaca': 14, 'tgacat': 14, 'gacata': 15, 'acatag': 13, 'catagg': 15, 'ataggc': 15, 'taggct': 18, 'aggctg': 10, 'ggctgt': 13, 'gctgtt': 19, 'ctgttg': 17, 'tgttgc': 17, 'gttgct': 20, 'ttgcta': 11, 'tgctag': 16, 'gctagc': 21, 'ctagct': 21, 'tagctc': 13, 'agctca': 12, 'gctcag': 9, 'ctcagg': 11, 'tcaggt': 19, 'caggtt': 18, 'aggttt': 18, 'ggtttg': 14, 'gtttgc': 12, 'tttgcg': 17, 'ttgcgg': 14, 'tgcggg': 14, 'gcgggt': 25, 'cgggta': 19, 'gggtac': 21, 'ggtacg': 14, 'gtacgg': 12, 'tacggt': 12, 'gtggga': 21, 'tgggat': 13, 'gataac': 15, 'taacca': 16, 'aaccac': 7, 'accacc': 13, 'ccaccc': 12, 'cacccc': 8, 'accccc': 10, 'ccccct': 8, 'cccctt': 13, 'cccttg': 14, 'ccttgc': 9, 'cttgct': 13, 'tgctac': 12, 'gctacc': 12, 'ctaccc': 16, 'cccatc': 12, 'ccatca': 12, 'catcac': 12, 'ggaaag': 18, 'aaagct': 14, 'aagctc': 15, 'gctcac': 8, 'ctcacc': 21, 'tcacca': 11, 'caccat': 10, 'accatt': 13, 'ccattc': 12, 'cattcc': 13, 'ttccgt': 14, 'tccgtt': 15, 'ccgttt': 8, 'tttgac': 11, 'ttgact': 10, 'tgacta': 10, 'gactac': 15, 'actacc': 18, 'ctaccg': 15, 'taccgt': 15, 'accgtt': 14, 'ccgtta': 16, 'gttagc': 15, 'ttagcg': 11, 'tagcgc': 15, 'agcgcc': 20, 'gcgccc': 15, 'ccctat': 12, 'cctatg': 13, 'ctatga': 10, 'tatgag': 10, 'atgagt': 16, 'agtcta': 11, 'gtctaa': 8, 'tctaat': 13, 'ctaatt': 9, 'taatta': 17, 'ttattg': 15, 'tattgt': 15, 'attgtt': 16, 'ttgtta': 18, 'tgttag': 15, 'gttagg': 18, 'ttaggg': 17, 'tagggc': 10, 'agggcg': 12, 'gggcgc': 13, 'ggcgca': 13, 'gcgcat': 17, 'cgcatg': 11, 'atgact': 12, 'tgactt': 12, 'gacttc': 11, 'acttcc': 15, 'cttcct': 17, 'ttccta': 23, 'tcctaa': 18, 'cctaac': 18, 'ctaaca': 13, 'taacat': 12, 'catgtg': 11, 'atgtgt': 14, 'tgtgtg': 13, 'gtgtga': 16, 'gtgatg': 10, 'tgatgc': 15, 'atgctt': 14, 'tgcttt': 11, 'gctttt': 13, 'ttttca': 10, 'tttcag': 13, 'ttcagg': 14, 'tcaggg': 14, 'cagggc': 13, 'agggca': 10, 'ggcagg': 15, 'gcagga': 15, 'caggat': 17, 'aggata': 10, 'gatagt': 15, 'atagtg': 15, 'tagtgc': 18, 'agtgca': 14, 'gtgcac': 10, 'tgcact': 12, 'cactgg': 13, 'actggt': 14, 'ctggta': 12, 'tggtag': 11, 'ggtagt': 10, 'gtagta': 12, 'agtaca': 7, 'gtacat': 19, 'tacatg': 15, 'catgtc': 13, 'atgtcg': 14, 'tgtcgg': 12, 'gtcggt': 18, 'tcggta': 10, 'cggtac': 14, 'ggtaca': 17, 'gtacaa': 12, 'tacaac': 9, 'acaaca': 12, 'caacac': 6, 'aacaca': 14, 'acacac': 16, 'cacact': 11, 'acacta': 16, 'cactat': 9, 'actatt': 12, 'ctattc': 12, 'ttcaca': 12, 'tcacac': 19, 'acactc': 13, 'cactcc': 17, 'actcct': 13, 'cctaaa': 18, 'ctaaaa': 17, 'taaaaa': 9, 'aaaaaa': 8, 'aaaaac': 12, 'aaaaca': 17, 'aaacat': 16, 'aacata': 16, 'acatat': 22, 'catatg': 17, 'atatgc': 13, 'tatgcc': 15, 'atgcct': 17, 'tgccta': 13, 'gcctag': 9, 'cctagc': 15, 'ctagcg': 15, 'gcgggc': 15, 'cgggct': 10, 'gggctg': 15, 'ggctgc': 11, 'gctgcc': 11, 'ctgccg': 13, 'tgccga': 14, 'gccgac': 14, 'ccgacc': 14, 'cgaccg': 10, 'accgtg': 15, 'ccgtga': 22, 'cgtgat': 21, 'gtgatt': 19, 'tgattc': 18, 'gattcc': 18, 'attccc': 11, 'ttccct': 4, 'ccctct': 17, 'cctctt': 19, 'ctctta': 12, 'tcttac': 11, 'cttaca': 13, 'ttacac': 13, 'acacat': 16, 'cacatt': 19, 'acattg': 13, 'cattga': 15, 'attgaa': 22, 'ttgaac': 10, 'gaacgt': 23, 'aacgta': 11, 'acgtat': 16, 'cgtatt': 22, 'gtattg': 18, 'tattgg': 8, 'attggg': 7, 'ttggga': 10, 'tgggag': 11, 'gggagc': 11, 'ggagct': 15, 'gagctg': 16, 'agctgg': 23, 'gctgga': 16, 'ctggaa': 20, 'tggaag': 12, 'gaagac': 7, 'aagacg': 11, 'agacgt': 17, 'gacgtc': 23, 'acgtcg': 21, 'cgtcgg': 19, 'gtcggc': 14, 'tcggct': 14, 'cggctc': 13, 'ctctag': 14, 'tctagg': 24, 'ctaggt': 21, 'taggtt': 20, 'ggtttc': 16, 'gtttcc': 16, 'tttccc': 9, 'ttcccg': 15, 'tcccga': 14, 'cccgaa': 14, 'cgaatg': 14, 'gaatgt': 20, 'atgtca': 14, 'tgtcaa': 13, 'gtcaag': 16, 'tcaagt': 14, 'caagta': 13, 'aagtaa': 11, 'gtaaaa': 14, 'aaaaag': 10, 'aaaagc': 12, 'agcacc': 8, 'gcaccg': 17, 'caccgt': 17, 'accgtc': 12, 'ccgtca': 14, 'cgtcat': 14, 'gtcatt': 17, 'tcattt': 16, 'catttc': 13, 'atttcc': 6, 'tttccg': 14, 'tccgca': 13, 'ccgcag': 10, 'cgcagt': 15, 'agttga': 18, 'gttgat': 21, 'tgatgt': 6, 'gatgta': 9, 'atgtat': 11, 'tgtatt': 10, 'gtattc': 16, 'tattcg': 14, 'attcgt': 22, 'ttcgta': 21, 'tcgtat': 17, 'attcag': 9, 'ttcagc': 16, 'tcagcg': 12, 'cagcgc': 22, 'agcgct': 12, 'gcgcta': 14, 'cgctat': 11, 'gctatt': 12, 'tattct': 16, 'attctt': 11, 'ttctta': 10, 'tcttaa': 11, 'cttaac': 13, 'ttaaca': 12, 'taacaa': 22, 'aacaac': 19, 'acaact': 14, 'caactg': 11, 'aactgt': 12, 'actgtg': 13, 'ctgtga': 11, 'tgtgaa': 14, 'gtgaac': 13, 'aactag': 12, 'actagt': 8, 'ctagta': 13, 'tagtaa': 15, 'agtaac': 12, 'gtaaca': 18, 'tcgaca': 14, 'cgacac': 14, 'gacacc': 12, 'acaccc': 14, 'caccct': 16, 'accctg': 15, 'ccctgt': 16, 'cctgta': 14, 'ctgtaa': 17, 'tgtaat': 15, 'gtaatg': 19, 'taatgc': 20, 'aatgcc': 16, 'atgcca': 13, 'tgccac': 12, 'gccacg': 14, 'ccacgg': 12, 'cggtgt': 15, 'ggtgtt': 15, 'gtgttt': 6, 'tgtttg': 16, 'gtttgg': 13, 'tttggt': 12, 'ttggtc': 15, 'tggtct': 18, 'ggtctg': 14, 'gtctgt': 11, 'tctgtg': 13, 'ctgtgg': 15, 'tgtggt': 7, 'gtggtc': 12, 'tggtca': 15, 'ggtcac': 18, 'gtcaca': 17, 'tcacat': 14, 'cacata': 14, 'acataa': 17, 'cataac': 19, 'ataacg': 15, 'taacgc': 18, 'aacgct': 16, 'acgcta': 16, 'cgctag': 20, 'gctaga': 19, 'ctagaa': 10, 'tagaag': 5, 'agaagc': 8, 'gaagca': 14, 'aagcat': 19, 'gcatgc': 10, 'catgcg': 9, 'atgcga': 17, 'gcgaca': 15, 'acagaa': 11, 'cagaag': 11, 'agaagt': 6, 'agttta': 14, 'gtttaa': 14, 'tttaaa': 13, 'ttaaaa': 10, 'taaaag': 13, 'aaaagg': 10, 'aaaggt': 13, 'aaggta': 16, 'aggtaa': 17, 'ggtaag': 16, 'gtaagt': 10, 'taagtt': 16, 'aagttc': 23, 'agttct': 19, 'gttcta': 18, 'ttctat': 19, 'tctatg': 8, 'ctatgt': 13, 'tatgtg': 13, 'tgattt': 12, 'gattta': 12, 'atttac': 19, 'tttaca': 13, 'tacact': 18, 'acactg': 10, 'actggg': 8, 'ctggga': 7, 'tgggaa': 12, 'gggaaa': 14, 'gaaatt': 14, 'aaattc': 17, 'aattca': 15, 'gaatgg': 18, 'aatggt': 14, 'atggta': 18, 'tggtac': 11, 'tacaag': 9, 'acaaga': 11, 'caagat': 10, 'aagatt': 10, 'agatta': 24, 'gattat': 16, 'attatc': 15, 'ttatcc': 17, 'tatcct': 14, 'atcctc': 16, 'tcctcg': 12, 'cctcgc': 16, 'ctcgct': 14, 'gctact': 18, 'ctactg': 13, 'tactgc': 17, 'actgcc': 13, 'ctgcca': 16, 'tgccaa': 10, 'gccaat': 8, 'ccaata': 14, 'caatac': 15, 'aatacg': 16, 'atacgg': 12, 'tacggc': 9, 'acggct': 10, 'cggctg': 12, 'ggctga': 14, 'gctgac': 9, 'ctgaca': 14, 'tgacaa': 12, 'gacaag': 14, 'acaagt': 9, 'caagtc': 13, 'aagtct': 13, 'tcttcg': 10, 'cttcgc': 13, 'ttcgcc': 16, 'tcgccc': 15, 'ctcaga': 13, 'tcagac': 12, 'agacac': 13, 'gacacg': 14, 'acacgt': 12, 'cacgtg': 9, 'acgtgc': 15, 'cgtgca': 11, 'gtgcag': 16, 'tgcaga': 21, 'gcagaa': 15, 'agaagg': 12, 'gaaggc': 11, 'aaggcc': 14, 'aggcca': 14, 'ggccaa': 15, 'ccaatc': 4, 'aatcgc': 9, 'atcgcc': 8, 'tcgccg': 14, 'cgccgc': 17, 'gccgct': 14, 'ccgcta': 22, 'gctaca': 17, 'ctacat': 12, 'tacatt': 13, 'acattc': 17, 'cattca': 14, 'attcat': 11, 'ttcatc': 21, 'tcatcc': 15, 'catcct': 16, 'atccta': 15, 'ctatgg': 15, 'tatggc': 20, 'tggctt': 16, 'ggcttg': 14, 'gcttga': 16, 'cttgac': 17, 'ttgaca': 14, 'tgacag': 22, 'cagaat': 9, 'agaata': 10, 'gaatac': 10, 'aataca': 12, 'atacaa': 5, 'tacaaa': 7, 'acaaat': 18, 'caaatt': 13, 'aaattt': 13, 'aatttg': 11, 'atttgg': 19, 'tttggc': 17, 'ttggca': 15, 'tggcaa': 14, 'ggcaaa': 11, 'gcaaac': 20, 'caaacc': 14, 'aaacca': 11, 'accaca': 16, 'ccacac': 13, 'actgat': 8, 'ctgatc': 13, 'tgatca': 22, 'gatcac': 19, 'atcact': 13, 'tcactc': 22, 'actccc': 14, 'ctccca': 23, 'tcccac': 10, 'cccacg': 21, 'acggtc': 13, 'cggtct': 12, 'gtctga': 19, 'tctgag': 19, 'ctgagt': 18, 'tgagtt': 17, 'gagttg': 9, 'gttggg': 8, 'ttgggt': 11, 'tgggta': 15, 'ggtact': 13, 'gtactg': 11, 'tactgt': 13, 'actgtt': 18, 'ctgtta': 17, 'ttaggt': 12, 'taggtc': 15, 'aggtct': 14, 'ggtcta': 19, 'gtctat': 10, 'tctatc': 17, 'ctatct': 14, 'tatctg': 19, 'atctga': 14, 'ctgaaa': 14, 'tgaaaa': 13, 'gaaaaa': 15, 'aaaaat': 8, 'aaaata': 14, 'aaatat': 14, 'aatatg': 20, 'atatgg': 18, 'tatggt': 16, 'atggtg': 15, 'tggtgc': 13, 'ggtgca': 16, 'gtgcat': 18, 'tgcatt': 12, 'gcattg': 15, 'cattgc': 14, 'tgcccg': 13, 'gcccgg': 18, 'cccgga': 12, 'ccggag': 12, 'cggagc': 22, 'gagctc': 14, 'agctcg': 7, 'gctcgg': 12, 'ctcggc': 11, 'tcggcg': 16, 'cggcgc': 14, 'ggcgcc': 16, 'gcgcca': 14, 'cgccat': 7, 'gccatt': 13, 'ccattt': 15, 'catttt': 18, 'attttg': 10, 'ttttgc': 11, 'tttgca': 15, 'ttgcat': 20, 'tgcatg': 13, 'gcatgt': 7, 'atgtcc': 8, 'tgtccc': 11, 'gtcccc': 9, 'tccccg': 6, 'ccccgt': 12, 'cccgtt': 17, 'gttaat': 22, 'ttaatc': 12, 'taatcc': 15, 'aatccg': 10, 'atccgg': 16, 'tccggg': 15, 'ccgggt': 18, 'cgggtc': 14, 'gggtca': 16, 'ggtcat': 9, 'tcattg': 16, 'cattgt': 19, 'attgtg': 17, 'tgtgct': 18, 'gtgctc': 12, 'tgctcg': 11, 'gctcga': 9, 'ctcgaa': 11, 'tcgaac': 15, 'cgaacc': 16, 'cccgta': 11, 'ccgtat': 23, 'attgcg': 16, 'ttgcgc': 18, 'tgcgcc': 16, 'gcgccg': 17, 'cgccgt': 10, 'gccgtg': 14, 'cgtgaa': 13, 'gtgaag': 14, 'tgaaga': 18, 'gaagag': 21, 'agagca': 15, 'gagcat': 10, 'agcatt': 12, 'gcattt': 10, 'catttg': 11, 'tttggg': 14, 'ttgggc': 12, 'tgggcg': 9, 'ggcgct': 16, 'ctactc': 19, 'tactct': 13, 'actcta': 10, 'ctctaa': 15, 'tctaag': 16, 'aagaga': 19, 'agagat': 26, 'gagatg': 20, 'agatgc': 12, 'gatgca': 15, 'atgcag': 16, 'gcagat': 15, 'atatca': 16, 'tatcaa': 18, 'atcaac': 21, 'tcaact': 18, 'caacta': 15, 'aactat': 12, 'actatc': 8, 'ctatcg': 15, 'tatcgc': 13, 'atcgca': 10, 'tcgcag': 14, 'cgcaga': 13, 'gcagac': 14, 'acaccg': 18, 'cgtatc': 21, 'gtatcg': 15, 'tatcgt': 15, 'atcgtt': 6, 'tcgttg': 12, 'cgttgt': 13, 'gttgtt': 8, 'ttgttg': 10, 'tgttga': 11, 'gttgaa': 7, 'ttgaat': 13, 'tgaatg': 12, 'aatgga': 12, 'atggag': 11, 'ggagag': 9, 'agagct': 11, 'gagctt': 16, 'agctta': 15, 'gcttat': 16, 'cttatc': 16, 'ttatca': 11, 'tatcat': 15, 'atcatg': 12, 'tcatgt': 12, 'cggttc': 15, 'ggttcg': 19, 'gttcga': 19, 'ttcgac': 13, 'tcgacc': 11, 'accatg': 11, 'catgat': 9, 'atgata': 11, 'tgatac': 20, 'gatact': 10, 'atacta': 10, 'actact': 13, 'actctg': 15, 'gtgaaa': 13, 'gaaagg': 16, 'aaaggg': 16, 'aagggc': 9, 'gggcaa': 8, 'ggcaag': 8, 'gcaaga': 7, 'aagata': 9, 'agataa': 12, 'gataat': 17, 'ataatc': 15, 'taatct': 12, 'aatctt': 11, 'atcttg': 22, 'cttggt': 12, 'ttggtt': 11, 'tggttg': 13, 'gttgcg': 22, 'tgcgca': 16, 'gcgcac': 15, 'cgcacc': 15, 'gcacct': 11, 'cacctt': 10, 'ccttgt': 14, 'cttgtc': 17, 'ttgtca': 18, 'tgtcat': 18, 'gtcatg': 20, 'tgtgac': 11, 'gtgacc': 11, 'tgaccg': 16, 'gaggcc': 17, 'aggccg': 16, 'ggccgg': 15, 'gccgga': 21, 'ccggat': 21, 'ggatat': 19, 'gatata': 20, 'atataa': 13, 'tataat': 15, 'ataatt': 22, 'taattg': 12, 'aattga': 18, 'ttgaag': 11, 'tgaagc': 18, 'aagcag': 13, 'agcagc': 13, 'gcagcc': 15, 'gccaaa': 15, 'ccaaat': 18, 'aaatta': 5, 'ttattt': 12, 'tatttc': 15, 'ttctgt': 14, 'tgtgga': 14, 'gtggag': 12, 'tggagg': 15, 'ggagga': 16, 'gaggac': 14, 'aggaca': 12, 'ggacac': 12, 'gacaca': 11, 'acatac': 12, 'catacg': 11, 'atacgc': 17, 'tacgcc': 20, 'acgccc': 17, 'cgcccg': 12, 'gcccga': 7, 'ttcagt': 15, 'tcagtc': 15, 'cagtcc': 13, 'agtcct': 12, 'gtcctt': 11, 'tccttt': 16, 'cctttc': 18, 'ctttca': 20, 'tcaggc': 13, 'caggcg': 13, 'aggcga': 13, 'ggcgag': 10, 'gcgagc': 11, 'cgagct': 13, 'agcttc': 16, 'gcttca': 15, 'cgaaca': 17, 'gaacac': 14, 'aacacg': 16, 'acacgg': 14, 'cggtcg': 8, 'ggtcgt': 11, 'gttgtc': 19, 'gtcgtc': 15, 'tcgtca': 14, 'cgtcag': 16, 'gtcagg': 12, 'caggca': 11, 'aggcac': 21, 'ggcacg': 19, 'gcacgc': 12, 'cacgct': 11, 'tagaca': 14, 'acacgc': 16, 'cacgca': 15, 'acgcaa': 14, 'cgcaag': 17, 'gcaagg': 18, 'aggcag': 20, 'ggcagc': 12, 'gcagcg': 12, 'cagcgg': 19, 'gggtag': 11, 'ggtagg': 18, 'gtaggc': 18, 'ggctcg': 13, 'gctcgt': 13, 'ctcgtt': 17, 'tcgttc': 17, 'cgttcg': 12, 'gttcgc': 15, 'ttcgcg': 15, 'tcgcgt': 16, 'gtgtcc': 10, 'gtccct': 10, 'tccctg': 8, 'ccctgg': 7, 'cctgga': 14, 'tggaac': 22, 'ggaacg': 20, 'gaacgc': 17, 'aacgca': 13, 'acgcag': 18, 'gcagtg': 19, 'cagtgc': 11, 'agtgcc': 7, 'gtgccc': 14, 'cccgat': 7, 'ccgata': 10, 'cgatac': 10, 'gataca': 8, 'atacac': 13, 'tacacc': 15, 'caccgc': 18, 'accgca': 13, 'ccgcac': 15, 'cgcaca': 16, 'gcacat': 19, 'cacatg': 14, 'acatgg': 15, 'catgga': 15, 'atggac': 6, 'tggaca': 6, 'gacact': 11, 'cactcg': 19, 'actcgg': 10, 'tcggac': 15, 'cggacc': 20, 'ggaccc': 14, 'gacccg': 6, 'acccgc': 10, 'cccgct': 13, 'ccgctt': 15, 'cgcttc': 15, 'gcttcg': 11, 'cttcgt': 12, 'tcgtaa': 19, 'cgtaaa': 15, 'taaaac': 17, 'aaacaa': 12, 'acaacc': 15, 'caaccg': 13, 'aaccgc': 16, 'accgcg': 12, 'ccgcgg': 19, 'cgcggg': 21, 'gcgggg': 12, 'cggggt': 13, 'ggggtt': 15, 'gggtta': 15, 'ggttac': 15, 'gttact': 18, 'ttactg': 17, 'actgct': 20, 'ctgcta': 15, 'tgctaa': 9, 'gctaaa': 11, 'ctaaag': 14, 'taaaga': 11, 'aaagac': 17, 'agacga': 14, 'gacgaa': 17, 'acgaag': 12, 'cgaaga': 11, 'gaagat': 12, 'atttca': 14, 'cagtca': 9, 'agtcac': 13, 'gtcact': 15, 'tcactt': 21, 'cacttt': 11, 'actttg': 18, 'ctttgt': 8, 'tttgtt': 15, 'ttgttc': 14, 'tgttcg': 13, 'ttcgct': 10, 'tcgctc': 13, 'cgctct': 5, 'gctctg': 10, 'tctgat': 11, 'tgatct': 16, 'gatcta': 16, 'atctaa': 18, 'ctaagc': 10, 'taagcc': 17, 'aagcct': 7, 'agccta': 11, 'agcgcg': 17, 'gcgcgg': 11, 'cgcggc': 10, 'gcggca': 14, 'cggcat': 15, 'ggcatt': 11, 'atttgc': 12, 'tttgcc': 8, 'cccgac': 11, 'ccgact': 13, 'cgactc': 15, 'gactca': 20, 'actcat': 18, 'tcataa': 12, 'cataat': 16, 'ataatg': 16, 'taatgt': 15, 'aatgta': 13, 'atgtag': 19, 'tgtagc': 20, 'gtagcg': 8, 'gcgctt': 17, 'cgctta': 11, 'gcttag': 17, 'cttagt': 16, 'ttagtc': 17, 'agtcga': 13, 'gtcgac': 14, 'actatg': 12, 'tatgga': 12, 'atggaa': 20, 'ggaata': 18, 'aataag': 9, 'ataaga': 10, 'taagat': 9, 'agattc': 13, 'gattcg': 18, 'attcgc': 16, 'cgcgta': 9, 'gcgtac': 9, 'cgtact': 10, 'ctgttt': 14, 'ttcggg': 10, 'tcgggc': 14, 'cgggcg': 14, 'gggcga': 7, 'ggcgac': 16, 'cgacct': 18, 'gacctt': 18, 'accttc': 12, 'ccttcg': 12, 'cttcga': 12, 'ttcgaa': 15, 'cgaagg': 12, 'aaggcg': 13, 'aggcgc': 13, 'gctatg': 14, 'ggctat': 13, 'gctatc': 16, 'atctcc': 17, 'tctcct': 21, 'ctcctt': 18, 'cctttg': 8, 'gtcgga': 11, 'tcggag': 14, 'agctcc': 22, 'gctcct': 19, 'tcctag': 15, 'ctagca': 14, 'agcatc': 17, 'atcgat': 14, 'tcgatt': 17, 'cgatta': 19, 'attatg': 13, 'ttatgg': 13, 'tatggg': 10, 'atgggc': 17, 'tgggct': 15, 'gggctt': 15, 'ggctta': 16, 'cttagg': 19, 'tagggt': 15, 'agggta': 17, 'gggtaa': 15, 'gtaagg': 11, 'taaggt': 11, 'aggtag': 16, 'gtaggt': 17, 'ggtctt': 11, 'tctttg': 9, 'ctttgg': 12, 'tggcat': 13, 'catcgc': 17, 'atcgct': 13, 'ctacgc': 12, 'acgccg': 13, 'cgccga': 14, 'gccgat': 16, 'ccgatt': 14, 'cgattc': 16, 'attcgg': 10, 'gggcgg': 12, 'ggcggc': 10, 'cggctt': 9, 'ttagtt': 11, 'gttatc': 15, 'ttatcg': 17, 'tatcgg': 15, 'atcggg': 14, 'cgggcc': 16, 'gggccc': 13, 'ggcccc': 15, 'gccccg': 16, 'ccccgg': 14, 'cccggg': 14, 'ccgggg': 11, 'cggggg': 17, 'gggggt': 14, 'ggggta': 12, 'gggtat': 16, 'ggtatg': 10, 'gtatga': 13, 'tatgaa': 13, 'atgaag': 12, 'tgaagg': 12, 'gaaggg': 8, 'aagggt': 15, 'agggtc': 16, 'gggtcg': 12, 'ggtcgg': 9, 'cggtat': 12, 'ggtatc': 12, 'atcgga': 25, 'cggagg': 16, 'ggaggc': 15, 'gcactt': 8, 'cactta': 14, 'acttaa': 12, 'cttaag': 16, 'ttaagg': 11, 'taaggc': 16, 'ggcgat': 12, 'gcgatc': 14, 'cgatca': 14, 'atcaca': 15, 'acatta': 13, 'cattac': 14, 'attacc': 11, 'ttaccg': 8, 'accgac': 14, 'ccgacg': 15, 'cgacgc': 10, 'gacgca': 18, 'aggccc': 14, 'cccccc': 7, 'ccccca': 15, 'ccccag': 10, 'ccagct': 20, 'cagctt': 13, 'agcttg': 17, 'gcttgc': 11, 'cttgca': 11, 'tgagta': 15, 'gagtat': 14, 'agtatt': 11, 'gtattt': 15, 'tatttg': 11, 'atttgt': 6, 'tttgta': 10, 'ttgtaa': 16, 'tgtaag': 14, 'gtaaga': 15, 'taagac': 15, 'aagact': 12, 'agactt': 6, 'gacttg': 17, 'acttgc': 9, 'ttgctg': 10, 'tgctga': 11, 'cagacc': 9, 'agacca': 9, 'gaccag': 7, 'cagagc': 9, 'gagcac': 11, 'acgctt': 11, 'gcttaa': 14, 'ttaaga': 14, 'taagaa': 16, 'aagctt': 16, 'tatgct': 7, 'atgcta': 12, 'ctaagg': 13, 'ggcacc': 15, 'gcacca': 10, 'caccaa': 13, 'accaaa': 17, 'ccaaaa': 9, 'caaaat': 13, 'aaaatc': 17, 'aaatca': 16, 'aatcac': 13, 'tcacaa': 14, 'cacaag': 14, 'acaagc': 11, 'caagca': 10, 'aagcaa': 7, 'agcaaa': 13, 'gcaaat': 5, 'tttcct': 22, 'ttcctt': 14, 'tccttc': 16, 'ttcacc': 19, 'tcaccg': 19, 'caccgg': 11, 'accggc': 15, 'ccggct': 18, 'tcatgg': 20, 'ggaaca': 14, 'aacatt': 16, 'ccgcaa': 13, 'gcaagt': 17, 'aagtat': 9, 'atcaag': 19, 'aagtac': 6, 'agtact': 10, 'gtactt': 14, 'tacttc': 14, 'ttccat': 17, 'tccatc': 11, 'catcaa': 12, 'tcaacc': 17, 'cgcgga': 22, 'gcggaa': 18, 'cggaag': 8, 'ggaagc': 17, 'cttata': 12, 'tatagc': 14, 'tagcga': 12, 'agcgag': 17, 'gcgagg': 10, 'cgaggt': 11, 'gaggta': 7, 'ggtaaa': 10, 'aagaca': 10, 'cacggg': 12, 'gggcgt': 15, 'gcgtca': 11, 'tcatgc': 17, 'catgcc': 12, 'tgccag': 18, 'gccaga': 10, 'agatac': 12, 'tactag': 11, 'actagc': 11, 'tagctg': 11, 'agctga': 14, 'gctgag': 18, 'ctgagc': 17, 'tgagct': 22, 'gagcta': 15, 'agctaa': 15, 'ctaaac': 15, 'taaaca': 18, 'aaacag': 13, 'aacagg': 20, 'acagga': 17, 'aggatt': 15, 'ggatta': 13, 'ttatgt': 10, 'tatgtc': 10, 'tgtcgc': 15, 'gtcgcg': 18, 'tcgcgc': 13, 'cgcgcc': 16, 'gcgcct': 22, 'cgcctt': 20, 'ccttct': 18, 'cttcta': 15, 'ttctac': 14, 'ctgtgt': 10, 'tgtgtt': 7, 'gtgttg': 16, 'tgttgt': 19, 'ttgtcc': 14, 'tgtccg': 9, 'gtccgt': 14, 'tccgtc': 11, 'cagggg': 11, 'aggggt': 14, 'ggggtc': 20, 'ggtcgc': 11, 'cgcgca': 14, 'cgcatc': 17, 'gcatca': 17, 'catcat': 12, 'atcatc': 16, 'tcatca': 8, 'tcacgt': 16, 'acgtgt': 13, 'gtctta': 16, 'cttacg': 13, 'ttacgg': 11, 'acggcg': 9, 'cggcga': 12, 'ggcgaa': 11, 'gcgaat': 15, 'cgaatc': 15, 'gaatcg': 17, 'gctcgc': 10, 'ctcgcc': 14, 'gccgca': 12, 'agaaga': 9, 'agacat': 8, 'gacatt': 11, 'cattaa': 13, 'attaag': 17, 'gagcag': 24, 'agcagt': 23, 'gcagtc': 13, 'cagtct': 11, 'gcatat': 13, 'atatag': 9, 'tataga': 8, 'atagag': 13, 'tagagt': 12, 'agagta': 13, 'agtaat': 13, 'tgtagt': 14, 'gtagtt': 11, 'tagttg': 15, 'gttgag': 22, 'ttgagg': 19, 'gaggcg': 11, 'cacctc': 15, 'acctca': 15, 'cataag': 15, 'ataagc': 15, 'taagcg': 13, 'aagcga': 17, 'gcgaac': 9, 'ccggcc': 19, 'cggcct': 17, 'ggccta': 5, 'gcctaa': 15, 'cctaat': 15, 'ctaatg': 17, 'aatgcg': 23, 'atgcgt': 10, 'tgcgtt': 12, 'gcgttt': 12, 'cgtttc': 14, 'tttcca': 14, 'tccatt': 9, 'acgtta': 10, 'taggta': 18, 'ggtaac': 15, 'gtaact': 17, 'taacta': 15, 'actaac': 16, 'ctaacc': 20, 'acctcc': 7, 'tccgga': 17, 'cggatc': 14, 'ggatca': 17, 'tcacag': 9, 'cacagc': 13, 'acagcg': 11, 'agcggt': 9, 'gcggtt': 13, 'gttcgg': 9, 'ttcgga': 12, 'cggacg': 15, 'ggacgt': 27, 'cgttta': 12, 'gtttag': 13, 'tttagt': 10, 'ttagtg': 10, 'gaactc': 10, 'aactcg': 15, 'cgccgg': 18, 'gccggt': 19, 'ccggta': 13, 'tacgga': 17, 'acggag': 18, 'ggagta': 7, 'agtata': 14, 'gtataa': 12, 'tataag': 14, 'taagca': 11, 'agcaga': 12, 'cagact': 9, 'agactc': 17, 'gactcc': 7, 'tttcaa': 16, 'ttcaaa': 25, 'tcaaag': 17, 'caaagc': 16, 'aaagcg': 18, 'aagcgc': 14, 'cgccaa': 12, 'caataa': 12, 'ataact': 20, 'taactt': 13, 'tttcat': 13, 'tcctct': 13, 'cctctc': 17, 'ctctct': 12, 'tctctc': 11, 'ctctcg': 9, 'tctcgc': 12, 'ctcgca': 14, 'tcgcac': 10, 'cgcact': 10, 'gcacta': 12, 'ctattt': 13, 'ctgaag': 20, 'gaagga': 17, 'aaggac': 14, 'aggacg': 21, 'ggacga': 11, 'gaatca': 15, 'tcctcc': 14, 'taaacg': 3, 'aaacgg': 9, 'aacggc': 13, 'acggcc': 17, 'cggccc': 15, 'gcccct': 13, 'ccccta': 15, 'ccctaa': 12, 'ctaata': 13, 'taataa': 11, 'acgtca': 21, 'cgtcaa': 14, 'gtcaaa': 8, 'tcaaac': 13, 'caaact': 13, 'aaacta': 10, 'aacaag': 9, 'caagaa': 11, 'aagaat': 16, 'agaatg': 22, 'tgtacg': 19, 'tgccgt': 13, 'ccgtgc': 13, 'cgtgcg': 15, 'gtgcgg': 10, 'gaaagt': 16, 'aaagtt': 16, 'aagttg': 12, 'ttgatc': 16, 'gatcca': 11, 'atccaa': 12, 'tccaat': 7, 'acggtt': 9, 'ggttca': 21, 'aattcg': 15, 'ttcggc': 12, 'tatgtt': 13, 'atgttg': 14, 'gttgta': 15, 'gtaatt': 11, 'taattc': 8, 'gcgtga': 15, 'aagatc': 11, 'agatct': 16, 'atctac': 13, 'tctacc': 13, 'taccgc': 10, 'attcaa': 16, 'ttcaat': 15, 'caatcc': 10, 'atccga': 13, 'tccgag': 12, 'ccgagt': 9, 'cgagtg': 17, 'gagtgg': 28, 'agtggg': 15, 'tgggtt': 11, 'gggttc': 14, 'ggttcc': 12, 'gttcct': 16, 'ttcctg': 16, 'tcctgt': 14, 'cctgtg': 17, 'ctgtgc': 20, 'tgctca': 10, 'gctcat': 15, 'ataagt': 14, 'taagta': 10, 'agtacg': 11, 'acggca': 8, 'gcattc': 14, 'cattct': 17, 'attcta': 18, 'tctatt': 13, 'ctatta': 15, 'tattac': 12, 'attact': 15, 'ttactt': 15, 'tacttg': 11, 'acttga': 15, 'cttgaa': 12, 'tgaatt': 13, 'gaatta': 10, 'aattag': 11, 'attaga': 13, 'ttagaa': 12, 'tagaat': 13, 'agaatc': 10, 'aatcga': 12, 'atcgac': 13, 'tcgacg': 15, 'cgacga': 15, 'gacgac': 12, 'acgacg': 7, 'gacgcg': 13, 'acgcgt': 11, 'gcgttg': 13, 'cgttga': 13, 'atctag': 14, 'tctagt': 15, 'ctagtg': 11, 'tagtgt': 12, 'agtgtg': 11, 'gtgtgt': 9, 'tgtgtc': 8, 'tgtcca': 15, 'gtccat': 12, 'tccatg': 22, 'ccatgc': 14, 'tgcgaa': 14, 'gaattt': 14, 'aatttt': 18, 'attttt': 13, 'tttttt': 12, 'tttttg': 19, 'ttttgt': 12, 'tttgtg': 6, 'ttgtgt': 15, 'tgtgta': 21, 'gtacgt': 14, 'gctgat': 16, 'ctgata': 23, 'atacat': 14, 'tacata': 19, 'atatac': 17, 'tatacg': 9, 'acgcca': 12, 'cgccac': 11, 'ccactc': 15, 'actcgt': 20, 'ctcgta': 11, 'tcgtag': 8, 'agcata': 15, 'accata': 16, 'ccatag': 8, 'atagga': 16, 'taggaa': 18, 'aggaaa': 17, 'ggaaaa': 18, 'gaaaat': 12, 'aaatct': 11, 'aatcta': 16, 'tctaca': 15, 'ctacag': 12, 'tacagt': 8, 'acagta': 13, 'cagtaa': 18, 'gtaatc': 9, 'taatcg': 7, 'tcgctt': 12, 'cgcttt': 19, 'gctttg': 12, 'ctttgc': 17, 'ttgcca': 13, 'agttcc': 12, 'cctgaa': 11, 'gaaggt': 10, 'aaggtg': 11, 'aggtgg': 14, 'ggtgga': 16, 'gtggaa': 16, 'tggaaa': 17, 'ggaaac': 18, 'gaaact': 20, 'aaactt': 17, 'aacttg': 16, 'acttgt': 22, 'cttgtt': 11, 'tgttaa': 15, 'ttaacg': 16, 'aacgcg': 17, 'acgcga': 16, 'cgcgac': 10, 'gcgact': 17, 'cgactt': 19, 'gactta': 11, 'ttaagc': 17, 'aagcca': 15, 'agccag': 14, 'gccagg': 12, 'ccaggt': 8, 'caggtg': 19, 'aggtgc': 16, 'gacgtg': 17, 'acgtga': 18, 'tgaggt': 15, 'gaggtg': 11, 'tggatt': 14, 'ggattt': 14, 'atttat': 14, 'tttatg': 10, 'atgttc': 10, 'tgttca': 15, 'gttcat': 13, 'ttcata': 11, 'ataaca': 22, 'taacag': 16, 'aacagc': 13, 'acagct': 18, 'cagctg': 18, 'gatacg': 17, 'tacgct': 10, 'acgctc': 8, 'cgctcc': 13, 'ctttct': 11, 'ttctcg': 9, 'gctagg': 17, 'ctagga': 22, 'taggag': 13, 'aggagt': 14, 'agtatg': 10, 'gtatgg': 12, 'tgggca': 14, 'gggcac': 17, 'ggcaca': 18, 'gcacac': 15, 'cacaca': 15, 'attgat': 17, 'ttgata': 12, 'tgatat': 18, 'tatcag': 10, 'atcagg': 17, 'aggcgg': 18, 'gcggat': 13, 'ggatcg': 11, 'gatcgc': 9, 'tcgcat': 20, 'gcatcc': 19, 'cctatt': 13, 'tattaa': 12, 'attaaa': 20, 'ttaaac': 11, 'taaact': 10, 'aaactg': 15, 'aactga': 13, 'actgag': 18, 'gagagg': 6, 'aggcgt': 9, 'ggcgtt': 7, 'ttgttt': 8, 'tgttta': 11, 'tttaac': 15, 'taacgg': 13, 'ggctca': 9, 'gctcaa': 11, 'ctcaag': 13, 'tcaagg': 20, 'caagga': 18, 'aggacc': 11, 'ccgctc': 9, 'cgctca': 12, 'ctcatg': 14, 'atggcc': 12, 'tggccg': 12, 'ggccgt': 12, 'cgtgga': 14, 'gtggac': 16, 'tggacg': 11, 'gacgta': 17, 'cgtatg': 12, 'atgaat': 10, 'gaattg': 22, 'aattgc': 13, 'cacttg': 16, 'tgaata': 11, 'gaatat': 16, 'aatatc': 14, 'atcagc': 9, 'tcagct': 11, 'gctggg': 12, 'ctgggt': 9, 'gggtga': 10, 'ggtgaa': 11, 'gcgcgc': 13, 'gccgta': 13, 'ccgtag': 12, 'cgtagt': 11, 'tagtat': 11, 'gtatcc': 13, 'tatcca': 13, 'atccat': 15, 'tgcctc': 12, 'cctcac': 13, 'caccga': 18, 'accgaa': 16, 'ccgaag': 15, 'cgaagc': 15, 'gaagcc': 15, 'aagccc': 14, 'ccgatc': 16, 'cgatct': 15, 'gatctc': 14, 'tctgta': 21, 'ctgtac': 17, 'tgtact': 12, 'gtactc': 12, 'tactcc': 11, 'actccg': 8, 'ctccga': 15, 'tccgat': 11, 'ccgatg': 10, 'cgatgg': 11, 'gatgga': 12, 'atggat': 14, 'tggata': 12, 'acccaa': 13, 'cccaac': 17, 'ccaact': 10, 'tattag': 14, 'agacaa': 15, 'gacaaa': 16, 'acaaac': 7, 'caaaca': 10, 'caggaa': 17, 'aggaac': 9, 'ggaacc': 14, 'ttgtac': 19, 'acttct': 8, 'cttctg': 18, 'ttctgg': 13, 'tctggt': 17, 'tactta': 14, 'acttat': 9, 'cttatt': 13, 'tgttac': 18, 'cttact': 8, 'tactgg': 11, 'ctgggg': 14, 'tggggt': 13, 'gggttg': 22, 'ggttga': 15, 'aggcta': 8, 'cacgtc': 13, 'tcggtc': 6, 'ctttta': 16, 'ttttat': 16, 'aaatgg': 8, 'aatggc': 14, 'cctcta': 15, 'tgctcc': 19, 'gctcca': 14, 'ctccac': 13, 'tccacc': 13, 'ccaccg': 9, 'ccgtaa': 12, 'cgtaac': 16, 'gtaacc': 12, 'taaccc': 14, 'aacccc': 15, 'acccct': 9, 'cccctc': 11, 'cctcga': 13, 'ctcgac': 11, 'cgacat': 13, 'gacatc': 8, 'acatca': 7, 'cccttc': 11, 'ttctag': 16, 'tctaga': 10, 'atgggg': 8, 'ggggaa': 11, 'aagaag': 12, 'agtttt': 12, 'gttttt': 12, 'ggacaa': 11, 'caagcg': 19, 'aagcgg': 15, 'cgggag': 10, 'ggagcc': 20, 'gagccg': 10, 'agccgg': 21, 'gccggc': 18, 'ccggcg': 8, 'gcgaaa': 14, 'cgaaag': 11, 'aaagaa': 13, 'gaatga': 7, 'aatgac': 16, 'tgactg': 11, 'tgagac': 13, 'gagacc': 14, 'tggact': 16, 'ggactg': 13, 'gactgt': 16, 'gtaagc': 19, 'agccca': 16, 'gcccat': 16, 'cccatt': 17, 'ccatta': 8, 'cattat': 17, 'cgcacg': 10, 'acggac': 20, 'cgtaca': 12, 'tacaat': 12, 'acaatc': 13, 'tcgggg': 9, 'cggggc': 7, 'ggggcc': 11, 'ccgttg': 17, 'cgttgg': 10, 'gttggc': 11, 'catgca': 15, 'atgcat': 11, 'tgcatc': 21, 'catccc': 14, 'atcccc': 18, 'tcccct': 19, 'cccctg': 10, 'ccctgc': 14, 'cctgcg': 12, 'ctgcgg': 8, 'tgcgga': 10, 'gtccaa': 9, 'tccaag': 11, 'caaggt': 16, 'aggtac': 8, 'gtacac': 13, 'tacacg': 7, 'gtttct': 14, 'ctggtg': 13, 'tggtgg': 16, 'aacgtt': 21, 'cgttac': 9, 'tactga': 11, 'gacatg': 12, 'catggt': 18, 'atggtt': 19, 'tggtta': 15, 'agggct': 12, 'gggctc': 9, 'accccg': 11, 'ccggaa': 15, 'cggaac': 13, 'gaacag': 12, 'aacaga': 14, 'cagatg': 19, 'agatgg': 24, 'gatggt': 18, 'tagacg': 11, 'gacggc': 9, 'cggcac': 17, 'atggca': 16, 'ttcaac': 14, 'caactc': 17, 'aactca': 16, 'actcag': 14, 'caggtc': 12, 'aggtca': 12, 'ggtcaa': 12, 'gtcaat': 14, 'tcaatt': 13, 'aattta': 18, 'atttag': 17, 'tttagc': 12, 'ttagca': 15, 'tagcag': 14, 'agcagg': 15, 'gcaggc': 15, 'ggcggt': 17, 'cggttt': 11, 'ggtttt': 9, 'gtttta': 8, 'tttata': 14, 'tagttc': 16, 'gttctt': 15, 'ttcttt': 12, 'tctttc': 17, 'ttcaag': 14, 'cggatg': 14, 'ggatga': 15, 'ttagcc': 13, 'tagccc': 13, 'ccctac': 14, 'cctacg': 13, 'tacgac': 12, 'acgacc': 19, 'cgaccc': 16, 'gaccct': 15, 'ctgcgc': 11, 'tgcgct': 15, 'acctat': 11, 'ctatcc': 11, 'tagcaa': 17, 'agcaat': 13, 'gcaatc': 15, 'caatct': 13, 'atctat': 12, 'ctcctc': 11, 'ctctgc': 13, 'tctgct': 11, 'ctgctc': 15, 'ctcatt': 18, 'tcattc': 11, 'cattcg': 10, 'gtaaac': 9, 'aacatc': 14, 'acatct': 8, 'catctg': 8, 'atctgt': 17, 'tctgtt': 16, 'ttgctc': 17, 'tgctct': 12, 'gctctc': 14, 'ctctca': 9, 'tctcat': 14, 'ctcatc': 12, 'atccgt': 18, 'tccgtg': 17, 'ccgtgt': 13, 'tgtcta': 9, 'gtctag': 18, 'ctagat': 20, 'tagatc': 17, 'agatcg': 11, 'gatcga': 11, 'tcgata': 13, 'gatacc': 12, 'ataccc': 13, 'ccctga': 11, 'cctgac': 14, 'aaccga': 17, 'gcagta': 20, 'agtaag': 12, 'aagagt': 16, 'agagtt': 15, 'gttgac': 7, 'ttgacc': 13, 'tgacct': 15, 'gacctc': 9, 'cttctt': 10, 'ttcttc': 18, 'cttccc': 9, 'tcccgg': 10, 'tcctac': 14, 'cctaca': 10, 'tacagc': 15, 'gctgaa': 10, 'ctgaat': 14, 'tgaatc': 12, 'aatcct': 14, 'atcctg': 15, 'tcctgg': 19, 'ttgacg': 11, 'tgacgc': 11, 'gacgct': 8, 'acgctg': 10, 'cgctga': 13, 'acgagc': 18, 'gagcgc': 14, 'gctata': 12, 'ctataa': 19, 'tataac': 20, 'taacga': 11, 'aacgaa': 8, 'cgaacg': 10, 'ttgggg': 9, 'tggggg': 11, 'gggggc': 18, 'ggggct': 9, 'ggcttc': 10, 'cttcag': 12, 'caggga': 12, 'agggaa': 16, 'gaaacc': 14, 'aaacct': 17, 'aacctg': 17, 'acctga': 19, 'cctgat': 20, 'ctgatg': 8, 'atgcac': 8, 'actggc': 11, 'ctggcc': 12, 'ggcctt': 14, 'gcctta': 12, 'ccttaa': 16, 'acactt': 13, 'ttggtg': 13, 'gtgcaa': 10, 'tgcaaa': 15, 'gcaaag': 14, 'catatc': 11, 'atatcg': 8, 'cgcagc': 10, 'cagcgt': 9, 'agcgtt': 11, 'gcgttc': 4, 'gttcaa': 20, 'tcaaca': 10, 'caacat': 14, 'actcgc': 18, 'cttaga': 9, 'aatacc': 11, 'atacct': 13, 'tacctt': 10, 'accttt': 11, 'ctttcg': 17, 'tttcgg': 10, 'tcgaaa': 15, 'aaagga': 15, 'aaggag': 25, 'aggagc': 20, 'agctag': 21, 'tagata': 16, 'gatatg': 13, 'gggcat': 12, 'ggcata': 12, 'atatga': 16, 'tatgat': 15, 'atgatt': 12, 'ttctaa': 11, 'tctaac': 8, 'ctaacg': 15, 'cgcttg': 10, 'ttgcaa': 10, 'aaccag': 13, 'accagt': 11, 'ccagtt': 14, 'cagttt': 14, 'gttttg': 6, 'gcacga': 13, 'acgaaa': 8, 'aaaggc': 7, 'ggagtg': 14, 'gagtgt': 9, 'agtgtc': 10, 'gtgtca': 12, 'tgtcag': 16, 'agttgc': 18, 'ttgctt': 14, 'tgctta': 10, 'taaggg': 10, 'aagggg': 14, 'aggggc': 12, 'ggggcg': 12, 'ggcgtg': 16, 'tgatgg': 13, 'tggtat': 16, 'atctca': 10, 'tctcaa': 13, 'tcaata': 14, 'cgcgaa': 12, 'cgaaac': 10, 'gaaacg': 10, 'aaacgt': 12, 'aacgtc': 16, 'acgtct': 15, 'cgtctc': 19, 'gtctca': 16, 'catgct': 15, 'tgcttg': 14, 'tgacac': 9, 'acacaa': 10, 'cacaac': 17, 'caacag': 17, 'acagca': 14, 'cagcat': 11, 'cgctcg': 13, 'cgttat': 9, 'ttataa': 14, 'aatgct': 13, 'tgcttc': 12, 'gcttcc': 15, 'cttccg': 9, 'cgcagg': 11, 'gcaggg': 15, 'aggggg': 13, 'aggtga': 8, 'ggtgac': 16, 'tgacca': 10, 'ccattg': 17, 'attgct': 7, 'tgctgt': 16, 'gctgtg': 13, 'gtgact': 11, 'gactag': 11, 'gcgtaa': 11, 'aaagat': 13, 'aagatg': 14, 'agatgt': 15, 'atgtaa': 13, 'tgtaac': 15, 'taactg': 16, 'aactgg': 13, 'actgga': 10, 'gaagct': 20, 'aagctg': 18, 'gctggt': 15, 'ctggtt': 21, 'tggttc': 17, 'gttcgt': 16, 'ttcgtt': 17, 'cgttct': 14, 'tctacg': 13, 'tacagg': 13, 'aggaat': 20, 'ggaatg': 15, 'ctggat': 20, 'aggatc': 17, 'gatcag': 15, 'atcagt': 10, 'cagttc': 13, 'agttca': 23, 'caatca': 9, 'aatcaa': 15, 'atcaaa': 8, 'actagg': 9, 'tagttt': 11, 'gtttac': 10, 'tttact': 17, 'ttacta': 13, 'tactat': 15, 'tattta': 15, 'ttacga': 13, 'aattct': 15, 'cagcta': 16, 'gctagt': 18, 'ctagtt': 12, 'tagaga': 18, 'gatgcc': 12, 'aaccca': 12, 'ccagca': 11, 'cagcac': 8, 'agcact': 11, 'actgtc': 12, 'ctgtct': 15, 'tgtctg': 17, 'tctgcg': 9, 'ttatct': 20, 'gttatg': 11, 'ttatgc': 4, 'atgccg': 17, 'tgccgg': 14, 'acggat': 18, 'cggatt': 19, 'gattca': 13, 'cacccg': 12, 'gtgagc': 17, 'tgagcg': 13, 'cactac': 14, 'actacg': 9, 'caatat': 10, 'atatgt': 12, 'atgtgc': 15, 'gtgccg': 11, 'atcgta': 15, 'gcactc': 13, 'cactct': 10, 'ctgtag': 9, 'tgtaga': 17, 'gtagac': 13, 'cagtag': 10, 'agtagg': 15, 'ccgaac': 16, 'gatcaa': 15, 'gttctg': 15, 'tgcgcg': 11, 'gcgcga': 12, 'cgcgag': 12, 'cgagca': 19, 'cggaga': 11, 'ggagat': 17, 'gagatc': 13, 'agatca': 11, 'gatcat': 15, 'atgctc': 8, 'ctcgtc': 16, 'tcgtct': 16, 'cgtctg': 15, 'tacggg': 10, 'acggga': 11, 'gggaac': 13, 'ggaact': 9, 'aactcc': 13, 'ctcctg': 19, 'gacagg': 14, 'acaggg': 10, 'aaggtt': 14, 'aggttc': 25, 'ggttct': 19, 'gttctc': 16, 'ttctct': 13, 'tctcta': 17, 'tacgat': 13, 'acgatg': 8, 'cgatga': 16, 'gatgac': 11, 'atgacg': 13, 'gcagca': 10, 'cagcaa': 15, 'agcaag': 14, 'caagtg': 17, 'aagtgc': 6, 'agtgcg': 12, 'gtgcga': 18, 'gcgacg': 12, 'cgacgt': 16, 'cgtctt': 11, 'ttacat': 11, 'acatga': 13, 'taatat': 15, 'aatatt': 14, 'atattt': 12, 'atttcg': 17, 'tttcgc': 16, 'taatga': 15, 'tgacgg': 15, 'gacgga': 14, 'gtggtg': 18, 'tggtgt': 11, 'ggtgta': 8, 'gtgtaa': 8, 'gtaata': 17, 'atatct': 20, 'atctcg': 19, 'tctcgg': 13, 'gcttgg': 11, 'ttggct': 14, 'tcacta': 8, 'cactag': 7, 'actaga': 13, 'agatag': 19, 'ctgagg': 20, 'aaatac': 9, 'cgccca': 18, 'ccatcg': 11, 'atcgcg': 17, 'tcgcgg': 18, 'gggatg': 16, 'gatgtt': 11, 'atgtta': 13, 'caccta': 14, 'acctac': 12, 'ctacaa': 8, 'caagct': 13, 'aagcta': 19, 'agctac': 18, 'tcatcg': 22, 'catcgg': 19, 'tcgggt': 10, 'gtcgca': 11, 'cgcatt': 20, 'ttcgca': 19, 'gttccg': 13, 'ttccga': 10, 'tccgac': 11, 'gaccac': 14, 'cataga': 11, 'atagac': 5, 'agacta': 14, 'gtcatc': 10, 'atcaat': 12, 'tcaatg': 14, 'caatgc': 19, 'atgcgg': 13, 'aacgat': 8, 'acgatt': 8, 'ctacct': 15, 'tacctc': 16, 'ctcaac': 16, 'caaccc': 16, 'acccca': 11, 'ccccaa': 11, 'ccaacc': 12, 'caacca': 12, 'accagg': 9, 'ccaggg': 11, 'agggga': 15, 'ggaagg': 10, 'gttggt': 13, 'tggtcc': 9, 'ggtcct': 17, 'tgtgcg': 18, 'cgcaac': 13, 'gcaaca': 14, 'gattaa': 25, 'ttaaat': 20, 'ccgtcg': 12, 'ggtata': 14, 'gtatag': 18, 'atagat': 14, 'tagatt': 18, 'gattag': 12, 'attagc': 8, 'agcctg': 17, 'gcctga': 15, 'tgagcc': 12, 'gagcca': 10, 'ccaaag': 16, 'caaagt': 11, 'gggtgc': 12, 'caaatc': 15, 'gtgaga': 10, 'tgagaa': 11, 'gagaaa': 11, 'agaaac': 11, 'cttaat': 11, 'ttaatg': 13, 'atgcgc': 18, 'ttttcc': 19, 'ttccca': 11, 'tcccag': 14, 'ccagcg': 25, 'cttgag': 14, 'ttgagt': 18, 'gtcttg': 15, 'tcttgc': 19, 'cttgcc': 13, 'ttgccg': 12, 'tgtttc': 10, 'gtttca': 13, 'taagct': 21, 'cgtaag': 13, 'cctggc': 16, 'cctaag': 10, 'gcctgg': 14, 'tggcga': 17, 'aataaa': 10, 'cagctc': 13, 'tttcga': 13, 'acgttg': 11, 'ttggag': 13, 'tggagt': 10, 'gagtga': 10, 'attcct': 12, 'gaggag': 13, 'agtgac': 9, 'gtgaca': 15, 'acacga': 12, 'cacgag': 15, 'atagct': 12, 'agctct': 14, 'gctctt': 9, 'ctcttt': 12, 'ctttcc': 18, 'tcccaa': 19, 'cccaaa': 11, 'caaaga': 18, 'agcgca': 16, 'gcgcaa': 20, 'cgcaat': 15, 'gcaatt': 8, 'caatta': 16, 'aattac': 13, 'attaca': 14, 'ttacag': 12, 'acaggt': 20, 'caggta': 9, 'taacac': 14, 'ggattg': 17, 'gattga': 13, 'attgag': 15, 'tgaggg': 17, 'gaggga': 12, 'cagcct': 12, 'gcctcc': 8, 'cctccc': 11, 'ctccgc': 11, 'ccgcat': 10, 'catcca': 10, 'atccac': 6, 'acccac': 23, 'cccact': 12, 'ccactt': 11, 'cacttc': 12, 'acttcg': 14, 'ttgagc': 19, 'tgagca': 11, 'cattta': 16, 'acagtg': 6, 'cagtgt': 17, 'agtgta': 18, 'gtgtat': 14, 'tctcga': 10, 'ctcgat': 14, 'ataccg': 13, 'aaatgc': 5, 'tgcggc': 13, 'gcggcc': 11, 'gcctcg': 16, 'tcgctg': 9, 'gacggt': 7, 'ccgttc': 15, 'gaaaag': 16, 'aaaagt': 9, 'cgtcgt': 13, 'attgca': 14, 'ttgcac': 15, 'tgcaca': 12, 'cacacc': 21, 'caaaaa': 7, 'aaaacc': 15, 'aaaccg': 18, 'ctctcc': 15, 'caggcc': 14, 'ggccat': 12, 'attata': 14, 'atagca': 11, 'gaatct': 12, 'tttaag': 11, 'ttaagt': 18, 'tccccc': 13, 'cccggt': 10, 'ccggtc': 7, 'cggtca': 10, 'ggtcag': 14, 'gtcagt': 16, 'agtcaa': 13, 'gtcaac': 14, 'tcaacg': 19, 'caacga': 15, 'aacgag': 13, 'cgagtc': 14, 'gagtca': 13, 'ttcgag': 12, 'tcgagc': 15, 'cttggg': 14, 'ggttgg': 12, 'ggacta': 14, 'ctacca': 11, 'accaac': 13, 'caactt': 11, 'acttta': 12, 'ctttac': 12, 'tactaa': 5, 'tgaaac': 18, 'aactgc': 12, 'ctgctt': 12, 'gcttta': 9, 'ctttag': 11, 'tagcac': 6, 'agcaca': 13, 'cacacg': 16, 'acgcat': 11, 'tatctt': 23, 'atcttc': 16, 'tcttct': 21, 'ttctgc': 12, 'tctgcc': 17, 'ctgccc': 14, 'gccctt': 12, 'cccttt': 10, 'ctttga': 10, 'tttgag': 18, 'gattgc': 13, 'ttgcga': 16, 'cgagtt': 16, 'gagttc': 17, 'gatcgg': 13, 'accgcc': 14, 'ccgcct': 12, 'cgccta': 16, 'aaatga': 13, 'aatgag': 7, 'gagttt': 14, 'agtttc': 12, 'ccatgt': 16, 'gtctcg': 12, 'tctcgt': 14, 'cgttgc': 16, 'tgccgc': 12, 'gccgcg': 9, 'cacggc': 13, 'cggccg': 12, 'ggccga': 16, 'cgatcg': 12, 'cgattg': 12, 'gattgt': 15, 'attgtc': 13, 'tgtcac': 8, 'ttacct': 17, 'tacctg': 17, 'acctgg': 14, 'gaactg': 8, 'tttgct': 12, 'aacagt': 11, 'cgggac': 10, 'gggact': 13, 'ggactc': 15, 'gactcg': 15, 'tcgcct': 11, 'gcctac': 12, 'cacgcg': 17, 'acgcgc': 16, 'ggaggg': 12, 'agggac': 10, 'gggaca': 9, 'caagag': 15, 'agagaa': 13, 'gagaat': 15, 'gcatta': 16, 'ttacca': 16, 'taccat': 10, 'ataagg': 13, 'aaggtc': 9, 'aggtcg': 10, 'ggtacc': 10, 'ccaacg': 15, 'tattga': 22, 'tgagtg': 11, 'gagtgc': 8, 'gtgcgt': 16, 'aattgg': 11, 'attggt': 12, 'tggtga': 19, 'caaata': 13, 'aaataa': 13, 'ataaaa': 9, 'aggagg': 13, 'gagggc': 10, 'ggcggg': 11, 'ggtcga': 8, 'tcgagg': 12, 'cgaggc': 7, 'cactaa': 14, 'agtagt': 9, 'gtagtg': 16, 'tagtga': 12, 'tgattg': 14, 'attgac': 13, 'ggcctg': 15, 'cctggg': 15, 'ctgggc': 12, 'tcatta': 17, 'ttatat': 13, 'ttgaga': 13, 'gagagt': 13, 'agagtg': 13, 'tgaccc': 11, 'ctcgag': 11, 'aatggg': 12, 'atgggt': 16, 'tgcctg': 8, 'aaaaga': 16, 'tcaaat': 12, 'aaattg': 12, 'agcccg': 15, 'cctgca': 14, 'ctgcaa': 15, 'caaagg': 14, 'ggtgct': 15, 'gtgcta': 17, 'tgctat': 18, 'tcatct': 14, 'catctc': 15, 'gttaag': 16, 'agttcg': 15, 'ttcgat': 13, 'tcgatc': 14, 'tcctgc': 13, 'ggagtt': 12, 'gttttc': 10, 'ttttcg': 10, 'cattgg': 13, 'attgga': 14, 'tgagat': 9, 'gagata': 17, 'gatatt': 11, 'atatta': 9, 'attaac': 12, 'acaggc': 9, 'ggcaac': 15, 'gcaacg': 14, 'caacgc': 19, 'gcagct': 11, 'acacct': 13, 'cctagg': 13, 'taggac': 17, 'cgtcga': 18, 'gtcgat': 13, 'tcgatg': 9, 'cgatgt': 4, 'tgtaca': 19, 'acgatc': 12, 'gatctg': 23, 'catggg': 14, 'atggga': 13, 'tgggac': 15, 'gggacg': 17, 'ggacgc': 17, 'gacgcc': 8, 'ctcact': 17, 'cactca': 17, 'ctcagc': 11, 'tcagcc': 17, 'gccagc': 17, 'tgcccc': 15, 'tgcgat': 15, 'gcgatt': 20, 'atccca': 13, 'tccaac': 11, 'ccaaca': 13, 'acagag': 15, 'gatgcg': 18, 'tgcgag': 13, 'gcgaga': 12, 'cgagat': 14, 'gatggg': 18, 'tggagc': 8, 'gcccag': 15, 'gtggta': 10, 'cctttt': 16, 'tggctc': 14, 'tcgact': 12, 'tcagca': 12, 'aagtgt': 12, 'gcgcag': 7, 'caggag': 15, 'aggaga': 19, 'gagcgt': 10, 'agcgtc': 8, 'gtcagc': 16, 'agccac': 17, 'actcac': 22, 'agtgct': 8, 'tagtca': 14, 'aattaa': 13, 'gcatac': 14, 'catacc': 13, 'acctta': 19, 'ccttag': 15, 'cttagc': 16, 'ttagct': 12, 'tagctt': 13, 'agcttt': 11, 'cttttt': 15, 'ttttta': 6, 'atagta': 11, 'gtacag': 11, 'gcggtc': 10, 'aatctg': 13, 'atctgg': 16, 'tggtaa': 12, 'taagtg': 18, 'atttaa': 11, 'tttaat': 10, 'aatgat': 10, 'atgatc': 17, 'gatcct': 14, 'cctgtt': 14, 'ttgcgt': 18, 'tgcgtc': 12, 'gcgtct': 12, 'cgatat': 14, 'agtgtt': 11, 'gtgtta': 14, 'agaggg': 9, 'gagggt': 17, 'agggtg': 14, 'gggtgt': 8, 'gtgttc': 9, 'tgttcc': 13, 'ttttac': 12, 'ggagca': 11, 'aggcct': 11, 'catcgt': 11, 'atcgtc': 13, 'tcgtcg': 20, 'tcgtgg': 10, 'gaccca': 18, 'cccaag': 13, 'ccaagc': 13, 'cgggga': 12, 'gggaat': 17, 'gaatgc': 18, 'aatgca': 10, 'agtctc': 10, 'gtctcc': 8, 'tcctta': 13, 'gcgagt': 19, 'ggctcc': 18, 'gctccg': 18, 'ctccgt': 11, 'tcaagc': 14, 'aagcgt': 14, 'aaccaa': 17, 'accaat': 10, 'ccaatg': 10, 'caatga': 8, 'ccacga': 14, 'cacgac': 16, 'acgact': 8, 'cgactg': 11, 'gactgg': 6, 'ctggct': 12, 'ggctac': 11, 'ctactt': 15, 'tacttt': 17, 'tttagg': 14, 'ttagga': 14, 'caaatg': 12, 'atgatg': 10, 'tccgta': 14, 'acatcg': 13, 'cgcgtc': 9, 'cgtcac': 15, 'ctattg': 10, 'tgataa': 16, 'atacgt': 12, 'tacgta': 16, 'acgtac': 10, 'cgtacg': 6, 'gtacgc': 11, 'ctccat': 12, 'gttcag': 22, 'acacca': 13, 'aaggct': 8, 'gctccc': 20, 'tcccat': 13, 'atcatt': 16, 'tttcgt': 15, 'aggtta': 18, 'ggttaa': 16, 'cagatc': 16, 'ctgttc': 20, 'cgtggc': 10, 'gtggcc': 15, 'ccttcc': 10, 'ccttac': 14, 'ccgccg': 15, 'ccggac': 18, 'acgcgg': 14, 'ggcgta': 9, 'cgtaat': 14, 'caatgg': 11, 'gggagg': 5, 'cagtgg': 10, 'ggatgc': 16, 'catagc': 6, 'tagcta': 18, 'tatcta': 10, 'tctaaa': 15, 'aacttc': 12, 'acttca': 12, 'cacgta': 13, 'acgtag': 16, 'cgtaga': 8, 'gtagag': 11, 'ccatac': 9, 'cataca': 13, 'aaacac': 18, 'cacatc': 13, 'acatcc': 16, 'cagagt': 8, 'gagtac': 12, 'catatt': 17, 'aataat': 13, 'cgcgct': 12, 'gcgctc': 13, 'aatagg': 16, 'tgcgtg': 13, 'gcgtgg': 17, 'ataaac': 8, 'taaacc': 12, 'aaccta': 10, 'tatccg': 12, 'tgaacc': 11, 'ccgaaa': 13, 'cgaaat': 15, 'gaaata': 12, 'aaatag': 19, 'aataga': 12, 'attcga': 9, 'aggtcc': 10, 'ggtccc': 10, 'gtcccg': 12, 'ttacaa': 12, 'acaatt': 12, 'caattc': 9, 'tcgtac': 12, 'accagc': 15, 'gggtcc': 17, 'ggtcca': 10, 'gtccac': 11, 'tccact': 13, 'tacccc': 5, 'ctaagt': 8, 'ttaatt': 14, 'taattt': 20, 'atttta': 18, 'ttttaa': 12, 'taaatc': 11, 'aaatcc': 18, 'ccgggc': 9, 'gggccg': 11, 'gccgaa': 13, 'gaagtc': 9, 'aagtcg': 11, 'taggat': 12, 'ggatcc': 20, 'tcccgt': 16, 'cccgtc': 18, 'ccgtcc': 14, 'cgtccc': 9, 'gccaac': 9, 'caacgt': 13, 'gtcacg': 11, 'cgaaaa': 14, 'aaatcg': 12, 'gacctg': 17, 'ggggtg': 8, 'ggtgag': 10, 'gtatat': 9, 'atattc': 17, 'tatgca': 8, 'atgcaa': 13, 'tgcaag': 15, 'gtatgt': 11, 'gtatta': 11, 'tcgagt': 15, 'gtgtag': 15, 'agaccc': 11, 'cccggc': 20, 'ggccca': 9, 'gcccaa': 12, 'ggagac': 14, 'agacct': 14, 'ctgacc': 13, 'gaccgg': 11, 'accgga': 16, 'tgtgca': 12, 'gcagag': 11, 'gtgata': 19, 'tacgtg': 15, 'cgtgcc': 8, 'gtgcca': 9, 'tgccat': 11, 'cgcctg': 8, 'gcctgc': 9, 'cgatcc': 16, 'gatccg': 20, 'cgttcc': 14, 'gcaatg': 15, 'caatgt': 16, 'aatgtt': 22, 'ttgatt': 9, 'ttggcg': 18, 'tggcgc': 9, 'ctggca': 15, 'tggcag': 15, 'tggccc': 15, 'aactac': 8, 'taccgg': 13, 'agtggt': 15, 'gtggtt': 8, 'gttgca': 17, 'tgcacc': 9, 'acctcg': 15, 'cctcgt': 8, 'tcacgc': 12, 'cgcgat': 18, 'gatctt': 12, 'ttgcag': 12, 'tgcagt': 16, 'gccggg': 10, 'cgggtt': 22, 'cttgtg': 15, 'acaacg': 16, 'caacgg': 17, 'aacgga': 16, 'gtgcgc': 11, 'atggtc': 14, 'tggtcg': 9, 'gtcgta': 9, 'aaaccc': 9, 'ccatct': 14, 'catcta': 15, 'gagatt': 15, 'agggtt': 14, 'tgcaac': 10, 'caacaa': 12, 'caacct': 11, 'ctgact': 8, 'gacttt': 14, 'ctttaa': 12, 'cgtcgc': 10, 'gtagat': 14, 'agatcc': 19, 'gactgc': 9, 'ctgctg': 14, 'agcaac': 10, 'gatgat': 16, 'gataag': 14, 'ggttat': 13, 'tatatc': 10, 'aggact': 11, 'tcagta': 7, 'cagtat': 13, 'atgccc': 8, 'cctata': 15, 'ctatag': 19, 'tatagg': 19, 'taggcc': 10, 'ggccct': 18, 'gccctg': 15, 'ctgcag': 21, 'gtcata': 5, 'tcatac': 12, 'ccttat': 13, 'ataggt': 12, 'tattat': 9, 'tatcga': 12, 'taaagg': 11, 'aaacga': 8, 'atacga': 12, 'gctttc': 17, 'ccccgc': 9, 'cccgca': 10, 'gcaact': 12, 'gctaac': 10, 'aacgcc': 20, 'acgcct': 14, 'cttgcg': 11, 'tctcca': 10, 'ctccaa': 11, 'aagtcc': 11, 'gtccgc': 10, 'agattg': 11, 'ttgtgg': 11, 'agaacg': 12, 'ccaatt': 10, 'caattg': 8, 'tatgac': 14, 'gactat': 9, 'actata': 13, 'ctatac': 8, 'tacgca': 9, 'acattt': 17, 'attttc': 14, 'tcacct': 14, 'gcacag': 13, 'cacagt': 8, 'ctacgg': 13, 'cggaca': 13, 'tagaac': 6, 'agaact': 9, 'gcatct': 19, 'tcttca': 14, 'cttcat': 14, 'ttcatt': 9, 'tttcac': 15, 'acaagg': 14, 'aaggaa': 8, 'gaacgg': 15, 'aacggt': 12, 'ggtgtc': 11, 'tttttc': 16, 'agcgac': 11, 'catgtt': 9, 'gcgata': 11, 'aaacgc': 11, 'tggatc': 20, 'cgcctc': 14, 'gcctat': 9, 'gtaacg': 11, 'cgccag': 11, 'cagccg': 15, 'agccga': 9, 'gccgag': 10, 'cgagcc': 9, 'cccagg': 12, 'ccaggc': 10, 'tccaca': 11, 'actcca': 13, 'ctccag': 12, 'tccagc': 14, 'cagcga': 10, 'gatgag': 14, 'gtatac': 11, 'tatacc': 13, 'tcttgt': 9, 'tcttga': 14, 'cgtgac': 12, 'gtgacg': 11, 'acgggg': 17, 'tcttag': 15, 'gggtct': 15, 'tgaagt': 8, 'ggatac': 5, 'gacaat': 12, 'taacgt': 15, 'aacgtg': 16, 'gcgtcg': 7, 'tgggtc': 10, 'ggtctc': 14, 'cgagag': 17, 'aaagcc': 9, 'ctacgt': 15, 'cgtagg': 14, 'gcacaa': 13, 'cacaaa': 8, 'acaaaa': 9, 'caaaac': 12, 'aaaacg': 9, 'aacggg': 13, 'actaat': 9, 'aatccc': 14, 'cgtgct': 14, 'gtgctg': 19, 'tgctgc': 11, 'gctgca': 10, 'gtacga': 13, 'aaggga': 9, 'gggatc': 15, 'ggatct': 18, 'gagaga': 16, 'gatagc': 11, 'gggggg': 9, 'gggttt': 11, 'ttccaa': 12, 'tccaaa': 15, 'ttaata': 17, 'atgacc': 15, 'gacccc': 13, 'gtctac': 12, 'ggaatt': 21, 'ttcgtc': 17, 'gtcgaa': 11, 'gcataa': 11, 'ccacca': 14, 'gttacc': 12, 'taccac': 9, 'ccacat': 11, 'tctcac': 19, 'ggggat': 16, 'ttcctc': 14, 'tcctca': 10, 'tgtaaa': 10, 'ttactc': 11, 'tactca': 16, 'tcagaa': 10, 'gaagcg': 10, 'agtccc': 11, 'gtccca': 10, 'tagcgt': 8, 'agcgtg': 11, 'gtggcg': 9, 'ctcccc': 9, 'ccctta': 13, 'cttatg': 6, 'gtgaat': 11, 'tcgcaa': 10, 'ctcaaa': 11, 'cctact': 15, 'tactcg': 13, 'actcga': 14, 'agctgc': 12, 'gctgct': 13, 'atcgag': 11, 'cccaat': 13, 'gttatt': 10, 'tttatt': 15, 'ttcgtg': 10, 'taactc': 12, 'cctgcc': 11, 'ctgcct': 9, 'cctcca': 11, 'caccag': 9, 'agttgt': 9, 'acgggt': 10, 'tgcggt': 8, 'gcggtg': 8, 'cggtga': 14, 'ggtgat': 15, 'accggg': 8, 'ctcaca': 12, 'catact': 10, 'cattag': 10, 'ttagat': 14, 'cggact': 18, 'ctcgcg': 14, 'tcgcga': 17, 'ggtagc': 11, 'agcgga': 16, 'ggaggt': 6, 'gaggtt': 19, 'ttatta': 12, 'gccatc': 6, 'ttccac': 14, 'ccgcga': 7, 'atgagc': 6, 'agagag': 10, 'ggcccg': 15, 'gcccgc': 11, 'cccgcc': 7, 'aacacc': 10, 'catgaa': 10, 'tcggtg': 15, 'ggtgtg': 12, 'atacag': 13, 'gagtta': 20, 'agggag': 6, 'ccgcca': 8, 'gccata': 11, 'ccataa': 20, 'cataaa': 10, 'taaagc': 15, 'gcttct': 12, 'atcaga': 12, 'accctt': 13, 'ttatga': 13, 'aattgt': 12, 'tccata': 13, 'attagt': 15, 'agtcag': 11, 'gtcaga': 13, 'ctctat': 10, 'aactct': 6, 'cgtttt': 6, 'tacccg': 11, 'acccgg': 14, 'aatcag': 15, 'cagaac': 13, 'aatctc': 6, 'ctcgtg': 11, 'tcgtgc': 15, 'tacatc': 9, 'catctt': 16, 'atcttt': 16, 'cgattt': 12, 'tttcta': 9, 'atctgc': 16, 'ccacgt': 12, 'acgcac': 12, 'ggggga': 9, 'ctaggg': 11, 'ggtaat': 14, 'taatag': 13, 'acgtgg': 11, 'tgtgag': 17, 'tttacc': 11, 'aggttg': 11, 'taccta': 16, 'ctcttc': 14, 'cttctc': 15, 'ggggca': 13, 'gtccgg': 10, 'ctatat': 6, 'ccggtg': 12, 'gattgg': 13, 'gaaaca': 13, 'aacaaa': 15, 'ccgtct': 10, 'cgtcta': 8, 'tagtgg': 10, 'gttcca': 12, 'ttacgt': 14, 'tacgtc': 15, 'tacgcg': 10, 'aaaatg': 4, 'ccacag': 9, 'ggtatt': 17, 'tattcc': 10, 'attcca': 9, 'ccatat': 14, 'cgcaaa': 12, 'cagggt': 14, 'acaaag': 12, 'ataata': 8, 'taatac': 16, 'acctgc': 12, 'cctgct': 12, 'attggc': 12, 'acttag': 13, 'tagccg': 12, 'aggtat': 9, 'gtatgc': 11, 'gcttgt': 17, 'ccacct': 13, 'tctggc': 11, 'caaggg': 14, 'gaaatc': 15, 'ccgaga': 17, 'gattac': 10, 'aatgaa': 10, 'atgaaa': 12, 'tgaaat': 8, 'agatga': 13, 'gactct': 12, 'actctt': 12, 'tacgtt': 8, 'gcaaaa': 12, 'caaaag': 9, 'gatttt': 8, 'ttcccc': 9, 'cttgta': 19, 'ttgtat': 11, 'ccccac': 8, 'cccacc': 12, 'cccagt': 8, 'ccagta': 11, 'cgtgtt': 12, 'ctcggg': 13, 'ggccgc': 8, 'gccgcc': 11, 'cacctg': 12, 'cctggt': 9, 'ggtgcc': 14, 'tcttta': 14, 'cccaga': 9, 'tcatga': 7, 'gagaag': 7, 'cgatag': 7, 'gagact': 12, 'tgactc': 8, 'actcaa': 15, 'cccata': 11, 'attagg': 10, 'cctacc': 14, 'gcaccc': 10, 'cctgtc': 13, 'ctgtcc': 9, 'cgtggt': 14, 'gagcaa': 11, 'gcaacc': 8, 'aaccat': 14, 'tcgaat': 13, 'gaatag': 8, 'gcggta': 12, 'cgacaa': 16, 'ccttta': 12, 'ctttat': 12, 'tataca': 12, 'agaggt': 16, 'aggtgt': 12, 'ttgtga': 13, 'gttccc': 10, 'ggctgg': 11, 'gcttac': 5, 'tccagt': 16, 'acctgt': 18, 'ctggtc': 9, 'gtctgg': 14, 'tcaaga': 14, 'caagac': 7, 'gcgctg': 11, 'cgctgt': 11, 'tgttat': 13, 'cttcgg': 10, 'tcggaa': 18, 'taggtg': 9, 'atcggc': 14, 'tctccg': 13, 'ttatac': 11, 'cggtaa': 11, 'gtaaat': 10, 'taaata': 16, 'agtgaa': 13, 'gaacct': 9, 'cgacgg': 8, 'atactg': 11, 'acgtaa': 15, 'gtttcg': 9, 'ataaat': 12, 'tgtatg': 15, 'tccacg': 7, 'cacgat': 6, 'tcggca': 10, 'cggcca': 14, 'ggccag': 13, 'aaggat': 14, 'ctgtca': 11, 'gcccac': 12, 'tacgag': 14, 'ctagcc': 10, 'tagcca': 15, 'aaaact': 10, 'tagtag': 11, 'gtagga': 8, 'taaaat': 10, 'aaccct': 5, 'tatatg': 9, 'gcgtgc': 5, 'tggggc': 8, 'atttga': 9, 'gtacct': 15, 'ttccgg': 13, 'tgccca': 12, 'gcgtat': 14, 'aaagta': 9, 'aagccg': 13, 'agccgt': 11, 'gcccgt': 18, 'acccga': 9, 'acgaga': 14, 'ctcggt': 12, 'cgataa': 9, 'aatact': 11, 'atactc': 11, 'tccgct': 10, 'caccac': 16, 'agttac': 8, 'gttacg': 12, 'gcaggt': 11, 'ggtgcg': 10, 'ttcttg': 11, 'tttaga': 13, 'agaatt': 11, 'tccggt': 12, 'ttttga': 11, 'ccaaac': 15, 'aaccgt': 13, 'acaatg': 14, 'tgtcct': 6, 'tccttg': 10, 'aaagtc': 18, 'ccaaga': 11, 'gccaca': 9, 'cgagac': 15, 'tttacg': 12, 'acgtcc': 10, 'cgtcca': 14, 'ccacgc': 11, 'ggactt': 16, 'ttcatg': 10, 'gccagt': 17, 'ccagtg': 17, 'taaatt': 12, 'gtgtgg': 8, 'tgtggg': 11, 'gacgat': 7, 'gacaac': 12, 'atagcc': 10, 'tatact': 13, 'ctggac': 9, 'ggacgg': 9, 'gcggac': 13, 'gtttat': 15, 'tttatc': 19, 'catcag': 8, 'gtcctc': 8, 'gagcct': 16, 'ctcacg': 12, 'aatcgt': 11, 'ttaaag': 15, 'gagggg': 15, 'tcgttt': 6, 'tgcagg': 15, 'ctagag': 12, 'agagtc': 7, 'ctcccg': 15, 'atgttt': 18, 'ttaggc': 18, 'taggca': 17, 'tcccca': 7, 'ttgtag': 14, 'ggctag': 18, 'gagtag': 15, 'agtaga': 14, 'tagatg': 11, 'cagcag': 13, 'agctat': 13, 'cgcccc': 11, 'gccgtc': 9, 'tgttgg': 10, 'ttggta': 10, 'ttgtct': 14, 'ggtaga': 6, 'tcgcca': 6, 'actttc': 14, 'gggcta': 7, 'ctatgc': 10, 'tatgcg': 8, 'gaaaac': 10, 'gatttg': 13, 'gagacg': 15, 'agacgc': 9, 'tatgta': 10, 'cgggtg': 8, 'cgaggg': 15, 'gccgtt': 10, 'tggcca': 9, 'acctaa': 16, 'aaactc': 11, 'tgtttt': 9, 'tggttt': 14, 'atacca': 10, 'ccatgg': 11, 'ggacca': 12, 'attctc': 16, 'caagcc': 8, 'accact': 10, 'ttggat': 16, 'gtgctt': 7, 'ggttta': 15, 'gtccta': 9, 'attaat': 14, 'ccacaa': 11, 'ccggga': 9, 'ttaact': 15, 'cgcata': 10, 'gaccga': 15, 'tctata': 13, 'ggggac': 12, 'taagga': 11, 'aacaat': 13, 'gctgtc': 12, 'aggctt': 10, 'gaacaa': 10, 'gtgtcg': 12, 'cgtata': 15, 'cgcggt': 9, 'cggtcc': 6, 'ggtccg': 5, 'tagaaa': 13, 'agaaaa': 9, 'taggcg': 16, 'tagagc': 8, 'caaacg': 17, 'tgatag': 11, 'aacact': 12, 'agcctt': 11, 'ctgatt': 11, 'tgatta': 7, 'cagtac': 10, 'gcaagc': 12, 'gttaca': 8, 'tcgtcc': 11, 'cgtccg': 14, 'cggtgc': 14, 'gcccca': 5, 'ccccat': 9, 'cgctaa': 13, 'gtacta': 8, 'atcctt': 12, 'ggagcg': 15, 'agcgta': 11, 'atactt': 12, 'gggaga': 11, 'tccagg': 15, 'ccagga': 19, 'aagacc': 13, 'aagaac': 10, 'agaaca': 13, 'ccagtc': 10, 'gccatg': 8, 'agggcc': 8, 'agctgt': 14, 'cttaaa': 13, 'gccacc': 10, 'gctgta': 10, 'tacaga': 12, 'tctagc': 13, 'agccat': 8, 'gataga': 9, 'tgcagc': 13, 'agccgc': 9, 'ctaggc': 10, 'ccacta': 7, 'atctta': 8, 'tggctg': 12, 'cggcgg': 8, 'ggacat': 10, 'atagaa': 8, 'taagtc': 7, 'aagtca': 12, 'gttaaa': 10, 'taatgg': 15, 'tcaaaa': 10, 'ggtggc': 9, 'tataaa': 9, 'tgttct': 12, 'cgtgtg': 10, 'gtgtgc': 13, 'tttctt': 15, 'caggct': 9, 'acgagg': 8, 'ggcttt': 10, 'ttcaga': 11, 'tcagat': 18, 'tccctt': 10, 'acggta': 8, 'cggtag': 6, 'tcagag': 9, 'gatgtc': 9, 'gtcacc': 11, 'cgctgg': 5, 'tatttt': 11, 'gtcgcc': 8, 'cttcaa': 16, 'cacgcc': 8, 'tgtata': 7, 'gaacca': 11, 'attacg': 9, 'attgta': 16, 'cggcgt': 6, 'tagggg': 14, 'gactaa': 8, 'actaag': 7, 'aaaatt': 8, 'gccttt': 16, 'gggacc': 8, 'caggac': 10, 'acccta': 9, 'ttttag': 8, 'acgata': 6, 'accgat': 16, 'tcagga': 8, 'aatata': 7, 'tcccta': 10, 'tttgat': 7, 'acttgg': 14, 'ccagaa': 7, 'gtagaa': 7, 'cggcag': 5, 'cacaat': 10, 'gaccaa': 4, 'atgaga': 9, 'gaggtc': 11, 'ggacag': 7, 'tcttat': 9, 'gcctgt': 10, 'ttacgc': 8, 'cagaaa': 10, 'cggaat': 18, 'aagagg': 10, 'gtagct': 10, 'gggcct': 8, 'accacg': 7, 'cgacta': 5, 'agaaat': 12, 'gtaggg': 10, 'ggtggt': 11, 'cccaca': 8, 'acaata': 8, 'agtcat': 11, 'tgcaat': 8, 'ggcaga': 9, 'gtagtc': 5, 'aatagt': 8, 'ccgaca': 8, 'ggcgcg': 4, 'tctggg': 7, 'acatgc': 10, 'cacagg': 9, 'gcggcg': 7, 'acagtt': 11, 'ttcggt': 5, 'tcggcc': 11, 'tgtagg': 6, 'actctc': 3, 'ctaact': 4, 'agagga': 6}



```python
count_cutoff = 23
for kmer, count in kmer_counts.items():
    if count > count_cutoff:
        print(kmer + " : " + str(count))
```

    cccagc : 24
    ccggtt : 26
    atggct : 24
    ttctga : 26
    tctgaa : 24
    agcggg : 26
    gcgggt : 25
    tctagg : 24
    agatta : 24
    agagat : 26
    atcgga : 25
    gagcag : 24
    ggacgt : 27
    ttcaaa : 25
    gagtgg : 28
    agatgg : 24
    aaggag : 25
    aggttc : 25
    gattaa : 25
    ccagcg : 25



```python

```
