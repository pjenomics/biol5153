

```python
myseq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(myseq)
count_a = myseq.count('A')
count_t = myseq.count('T')

print("Length: " + str(length))
print("A count: " + str(count_a))
print("T count: " + str(count_t))
at_content = (count_a + count_t) / length
print("AT content: " + str(at_content))
```

    Length: 54
    A count: 16
    T count: 21
    AT content: 0.6851851851851852



```python
myseq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = myseq.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())
```

    tCTGtTCGtTTtCGTtTtGTtTTTGCTtTCtTtCtTtTtTtTCGtTGCGTTCtT
    tCaGtaCGtaatCGatatGataaaGCataCtatCtatatataCGtaGCGaaCta
    tgaGtagGtaatgGatatGataaaGgatagtatgtatatatagGtaGgGaagta
    tgactagctaatgcatatcataaacgatagtatgtatatatagctacgcaagta
    TGACTAGCTAATGCATATCATAAACGATAGTATGTATATATAGCTACGCAAGTA



```python
myseq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = myseq.find("GAATTC") + 1
frag2_length = len(myseq) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))
```

    length of fragment one is 22
    length of fragment two is 33



```python
myseq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#length = len(myseq)
#print("Length: " + str(length))
# determine the length of the sequenceprint
exon_1 = myseq[0:62]
exon_2 = myseq[90:123]
print("Exon 1 & 2: ", exon_1 + exon_2)
```

    Exon 1 & 2:  ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCATCGATCGATATCGATGCATCGACTACTAT



```python
myseq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
length_myseq = len(myseq)
coding = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCATCGATCGATATCGATGCATCGACTACTAT" 
length_coding = len(coding)
percent_coding = (length_coding/length_myseq)*100
print("Percent coding:", percent_coding)
```

    Percent coding: 77.23577235772358



```python
myseq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = myseq[0:62]
exon_2 = myseq[90:123]
intron_1 = myseq[62:90]
print(exon_1 + intron_1.lower() + exon_2)
```

    ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGatcgatcgatcgatcgatcgatcatgctATCATCGATCGATATCGATGCATCGACTACTAT

