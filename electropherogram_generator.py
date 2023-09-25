import glob
from Bio import SeqIO
import matplotlib.pyplot as plt

# Function to get the list of nucleotides
def get_labels(num_points, file_path):
    
    # Read the .ab1 file and get PBAS1 data
    try:
        record = SeqIO.read(file_path, "abi")
        pbas1_data = record.annotations["abif_raw"].get("PBAS1", "")

        # Convert PBAS1 string to a list
        num_points = list(pbas1_data.decode())
    except Exception as e:
        print("Error processing the file:", str(e))

    return num_points

# Search for all .ab1 files in the current directory
ab1_files = glob.glob("*.ab1")

# Iterate over the found files
for file_path in ab1_files:
    print("Processing file:", file_path)

    # Read the .ab1 file and get electropherogram and PLOC1 data
    try:
        record = SeqIO.read(file_path, "abi")

        # Get electropherogram data
        channels = record.annotations["abif_raw"]["DATA9"], record.annotations["abif_raw"]["DATA10"], \
                   record.annotations["abif_raw"]["DATA11"], record.annotations["abif_raw"]["DATA12"]

        # Get PLOC1 data
        ploc1_data = record.annotations["abif_raw"].get("PLOC1", "")

        # Create a new figure for each file
        plt.figure()

        # Plot the electropherogram
        plt.plot(channels[0], label="DATA9 (G)", color="black")
        plt.plot(channels[1], label="DATA10 (A)", color="green")
        plt.plot(channels[2], label="DATA11 (T)", color="red")
        plt.plot(channels[3], label="DATA12 (C)", color="blue")

        plt.xlabel("Nucleotides")
        plt.ylabel("Intensity")
        plt.title("Electropherogram for file: " + file_path)
        plt.legend()

        # Set the labels on the x-axis using the get_labels() function
        x_ticks = []
        x_labels = get_labels(len(ploc1_data), file_path)

        for index in ploc1_data:
            if isinstance(index, int) and 0 <= index < len(channels[0]):
                x_ticks.append(index)

        plt.xticks(x_ticks, x_labels)

        plt.savefig(f"electropherogram_{file_path}.png")  # Save the figure as an image
        plt.close()
    except Exception as e:
        print("Error processing the file:", str(e))

    print()  # Print an empty line to separate the output between files
