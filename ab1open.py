
from Bio import SeqIO
import os

# Specify the path to the AB1 file in a current directiry
current_dir = os.getcwd()
ab1_file = os.path.join(current_dir, "Abl-mut_E9.ab1")

# Use SeqIO to read the genetic sequence from the AB1 file
sequences = SeqIO.parse(ab1_file, "abi")

# Iterate over all sequences in the file (usually an AB1 file contains a single sequence)
for sequence in sequences:
    # Print the genetic sequence
    print(sequence.seq)