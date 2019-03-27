

```python
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()
```


```python
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
```


```python
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")
```


```python
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)
```


```python
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
```


```python
print(header_1)
print(seq_1)
print(header_2)
print(seq_2)
print(header_3)
print(seq_3)
```

    ABC123
    ATCGTACGATCGATCGATCGCTAGACGTATCG
    DEF456
    actgatcgacgatcgatcgatcacgact
    HIJ789
    ACTGAC-ACTGT--ACTGTA----CATGTG



```python
print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2)
print('>' + header_3 + '\n' + seq_3)
```

    >ABC123
    ATCGTACGATCGATCGATCGCTAGACGTATCG
    >DEF456
    actgatcgacgatcgatcgatcacgact
    >HIJ789
    ACTGAC-ACTGT--ACTGTA----CATGTG



```python
print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2.upper())
print('>' + header_3 + '\n' + seq_3.replace('-', ''))
```

    >ABC123
    ATCGTACGATCGATCGATCGCTAGACGTATCG
    >DEF456
    ACTGATCGACGATCGATCGATCACGACT
    >HIJ789
    ACTGACACTGTACTGTACATGTG



```python
output = open("sequences.fasta", "w")
output.write('>' + header_1 + '\n' + seq_1)
output.write('>' + header_2 + '\n' + seq_2.upper())
output.write('>' + header_3 + '\n' + seq_3.replace('-', ''))
```




    31




```python
output = open("sequences.fasta", "w")
output.write('>' + header_1 + '\n' + seq_1 + '\n')
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')
```




    32




```python
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")
```
