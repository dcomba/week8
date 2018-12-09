#!/usr/bin/env python

#this script reads a DNA sequence and produces it's complement strand

#read user input of DNA sequence using ATGC syntax
sequence=input("Enter a DNA sequence using ATGC syntax with no spaces: ")
sequence=sequence.upper()

#reverse sequence string
revseq=sequence[::-1]

#create and print complement strand
for base in revseq:
	if base=="A":
		print('T', end='')
	elif base=="T":
		print('A', end='')
	elif base=="G":
		print('C', end='') 
	elif base=="C":
		print('G', end='') 


print()

# DB: Very good! Works well and is written cleanly.
