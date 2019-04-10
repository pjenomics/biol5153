#! /usr/bin/env python3

import csv

f = open("file.csv", "r")
reader = csv.reader(f)
data = open("output.csv", "w")
w = csv.writer(data)
for row in reader:
	my_row = []
	my_row.append(row[3])
	my_row.append(row[4])
	my_row.append(row[5])
	my_row.append(row[8])
	w.writerow(my_row)
