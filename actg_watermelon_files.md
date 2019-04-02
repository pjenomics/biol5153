

```python
fasta_file = 'watermelon.fsa'
fasta_file = open(fasta_file,'r')
sequence = next(fasta_file) 
fasta = fasta_file.read() 
length = len(fasta)
#print('my sequence is' + fasta) 
print(str(length))
```

    379237



```python
numA = fasta.count('A')
print(str(numA))
numC = fasta.count('C')
print(str(numC))
numG = fasta.count('G')
print(str(numG))
numT = fasta.count('T')
print(str(numT))
total = numA + numC + numT + numG
print(str(total))
```

    103995
    85546
    85409
    104286
    379236



```python
freqA = numA/length
freqC = numC/length
freqG = numG/length
freqT = numT/length
print ('Freq of A: %.2f' % freqA)
print ('Freq of C: %.2f' % freqC)
print ('Freq of G: %.2f' % freqG)
print ('Freq of T: %.2f' % freqT)
```

    Freq of A: 0.27
    Freq of C: 0.23
    Freq of G: 0.23
    Freq of T: 0.27



```python

```
