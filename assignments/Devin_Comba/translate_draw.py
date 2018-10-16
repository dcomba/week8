#!/usr/bin/env python

#this script prompts user to choose an action and enter a DNA sequence

print ("Choose one of the actions below by entering a number with no punctuation")
action = input ("(1) translate a protein-coding nucleotide sequence to amino acids -or- (2) randomly draw a codon from the sequence	")

DNAseq = input("Enter a DNA sequence with no spaces:	")
DNAseq =  DNAseq.upper()

#both options requre RNA codon, so this transcribes the DNA into an RNA sequence

RNAseq = DNAseq.replace("T","U")

#dictionary for translating RNA codons to amino acids

translate = {"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn",
             "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
             "AGA":"Arg", "AGC":"Ser", "AGG":"Arg", "AGU":"Ser",
             "AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
             "CAA":"Gln", "CAC":"His", "CAG":"Gln", "CAU":"His",
             "CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro",
             "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
             "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",
             "GAA":"Glu", "GAC":"Asp", "GAG":"Glu", "GAU":"Asp",
             "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
             "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
             "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
             "UAA":"Stop", "UAC":"Tyr", "UAG":"Stop", "UAU":"Tyr",
             "UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
             "UGA":"Stop", "UGC":"Cys", "UGG":"Trp", "UGU":"Cys",
             "UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

#if user chose action 1, the following applies. assuming the sequence is in 3-base codons, the script will convert the codons into amino acids
if action == "1":
	AAseq = ""
	if len(RNAseq)%3 == 0:
		for n in range(0, len(RNAseq), 3):
			if RNAseq[n:n+3] in translate:
				AAseq += translate[RNAseq[n:n+3]]
		print ("Amino Acid sequence: ")
		print (AAseq)

#if user chose action 2, the following applies. this produces a sequence of codons and then picks one to spit out. 
elif action == "2":
	codon = [RNAseq[i:i+3] for i in range(0, len(RNAseq), 3)]
	import random
	randomCodon = random.choice(codon)
	print (randomCodon)
