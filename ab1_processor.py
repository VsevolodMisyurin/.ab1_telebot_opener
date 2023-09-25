from Bio import SeqIO

def process_ab1_file(file_path):
    """Process the AB1 file and return the genetic sequence."""
    try:
        sequences = SeqIO.parse(file_path, "abi")

        # Iterate over all sequences in the file (usually an AB1 file contains a single sequence)
        for sequence in sequences:
            # Return the genetic sequence as a string
            return str(sequence.seq)
    except Exception as e:
        return f"Error processing file: {e}"