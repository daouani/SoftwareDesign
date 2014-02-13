# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: DINA AOUANI
"""

# you may find it useful to import these variables (although you are not required to use them)

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


    """1)  Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
import amino_acids
print amino_acids.codons
    
def coding_strand_to_AA(dna):
    list_aa = ""
    for i in range(0, len(dna), 3):
        curr_triplet = dna[i : i + 3]        
        for n in range(0, len(amino_acids.codons),1):
            if curr_triplet in amino_acids.codons[n]:
                list_aa += amino_acids.aa[n]
    return list_aa            
print coding_strand_to_AA('ATGGACTTT')

############################################

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    # YOUR IMPLEMENTATION HERE
    input = ["ATG", "ATGCEAFD", "FAS"]
    expected_output = ["MR", "RDS", "FF"]
    actual = []
    for i in input:
        actual.append(coding_strand_to_AA(i))
        print input 
        print actual
        print expected_output

############################################

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string"""
    dna="ATCG"
    b = list(dna)
    b.reverse()
    "".join(b)

    for n in range(0, len(b), 1):
        if b[n] == "A":
            b[n] = "T"
        elif b[n] == "C":
            b[n] = "G"
        elif b[n] == "T":
            b[n] = "A"
        elif b[n] == "G":
            b[n] = "C"
        
        print "".join(b) 

############################################  

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    input = ["dna"]
    expected_output = ["reversed_dna"]
    actual = []
    for j in input:
        actual.append(get_reverse_complement(j))
        print input 
        print actual
        print expected_output
    
############################################
    
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    for h in range(0, len(dna), 3):
        curr_triplet = dna[h : h + 3]    
        #for n in range(0, len(amino_acids.codons),1):
        if curr_triplet in amino_acids.codons[10]:
            return dna[0 : h]       
    return dna
print rest_of_ORF('ATGAGATAGG')

############################################
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    input = ["dna"]
    expected_output = ["rest of ORFs"]
    actual = []
    for k in input:
        actual.append(rest_of_ORF(k))
        print input 
        print actual
        print expected_output

############################################
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    i=0 
    ORF_list = []
    while i<len(dna):
        if dna[i : i+3] == "ATG":
            start_place = i                 
            current_ORF = rest_of_ORF(dna[start_place:])
            i += 3 + len(current_ORF)
            ORF_list.append(current_ORF)            
    return ORF_list

print find_all_ORFs_oneframe("ATGAGATAGATG")


############################################
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    input = ["dna"]
    expected_output = ["all non-nester ORFs"]
    actual = []
    for k in input:
        actual.append(find_all_ORFs_oneframe(k))
        print input 
        print actual
        print expected_output

############################################
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
     
############################################
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    input = ["dna"]
    expected_output = ["all non-nested ORFs"]
    actual = []
    for k in input:
        actual.append(find_all_ORFs(k))
        print input 
        print actual
        print expected_output

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE