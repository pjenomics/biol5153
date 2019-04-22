#! /usr/bin/env python3
accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455",
"xjhd53e", "45da", "de37dp"]


for acc in accs:
    if re.search(r"d.*e", acc):
        print("\t" + acc)

for acc in accs:
    if re.search(r"(d.e)", acc):
        print("\t" + acc)

for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print("\t" + acc)

 for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)

 for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)

for acc in accs:
    if re.search(r"\d{3,}", acc):
        print("\t" + acc)

for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)

import re
dna = open("dna.txt").read().rstrip("\n")
print(str(len(dna)))
all_cuts = [0]
# add cut positions for AbcI
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)
# add cut positions for AbcII
for match in re.finditer(r"GC[AG][AT]TG", dna):
    all_cuts.append(match.start() + 4)
# add the final position
all_cuts.append(len(dna))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)
for i in range(1,len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("one fragment size is  "  + str(fragment_size))
 