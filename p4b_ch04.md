

```python
file = open("input.txt")
for dna in file:
    print(dna)
```

    ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
    
    ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
    
    ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
    
    ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
    
    ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA
    



```python
file = open("input.txt")
for dna in file:
    last_character_position = len(dna)
    trimmed_dna = dna[14:last_character_position]
    print(trimmed_dna)
```

    TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
    
    ACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
    
    ATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
    
    ACTATCGATGATCTAGCTACGATCGTAGCTGTA
    
    ACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA
    



```python
file = open("input.txt")
output = open("trimmed.txt", "w")
for dna in file:
    last_character_position = len(dna)
    trimmed_dna = dna[14:last_character_position]
    output.write(trimmed_dna)
    print("processed sequence with length " + str(len(trimmed_dna)))
```

    processed sequence with length 43
    processed sequence with length 38
    processed sequence with length 49
    processed sequence with length 34
    processed sequence with length 48



```python
exon_locations = open("exons.txt")
for line in exon_locations:
    print(line)
```

    5,58
    
    72,133
    
    190,276
    
    340,398
    



```python
exon_locations = open("exons.txt")
for line in exon_locations:
    positions = line.split(',')
    print(positions)
```

    ['5', '58\n']
    ['72', '133\n']
    ['190', '276\n']
    ['340', '398\n']



```python
exon_locations = open("exons.txt")
for line in exon_locations:
    positions = line.split(',')
    start = positions[0]
    stop = positions[1]
    print("start is " + start + ", stop is " + stop)

```

    start is 5, stop is 58
    
    start is 72, stop is 133
    
    start is 190, stop is 276
    
    start is 340, stop is 398
    



```python
genomic_dna = open("genomic_dna.txt").read()
exon_locations = open("exons.txt")
for line in exon_locations:
    positions = line.split(',')
    start = positions[0]
    stop = positions[1]
    exon = genomic_dna[start:stop]
    print("exon is: " + exon)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-0d3a4d55961d> in <module>()
          5     start = positions[0]
          6     stop = positions[1]
    ----> 7     exon = genomic_dna[start:stop]
          8     print("exon is: " + exon)


    TypeError: slice indices must be integers or None or have an __index__ method



```python
start = int(positions[0])
stop = int(positions[1])
```


```python
coding_seq = exon1 + exon2 + exon3 + exon4
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-8dde1bfb83b7> in <module>()
    ----> 1 coding_seq = exon1 + exon2 + exon3 + exon4
    

    NameError: name 'exon1' is not defined



```python
genomic_dna = open("genomic_dna.txt").read()
exon_locations = open("exons.txt")
coding_sequence = ""
for line in exon_locations:
    positions = line.split(',')
    start = int(positions[0])
    stop = int(positions[1])
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
    print("coding sequence is : " + coding_sequence)
```

    coding sequence is : TCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
    coding sequence is : TCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
    coding sequence is : TCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
    coding sequence is : TCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

