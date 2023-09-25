import os
from Bio import SeqIO

def convert_ab1_file_to_txt(file_path):
    # Read the ABI file using SeqIO
    record = SeqIO.read(file_path, "abi")
    data = record.annotations["abif_raw"]

    # Extract data from the sections
    data9 = data.get("DATA9", [])
    data10 = data.get("DATA10", [])
    data11 = data.get("DATA11", [])
    data12 = data.get("DATA12", [])
    ploc1 = list(data.get("PLOC1", []))
    pbas1_raw = data.get("PBAS1", "")
    pbas1 = []

    # Convert PBAS1 to a list of characters
    if isinstance(pbas1_raw, bytes):
        pbas1_raw = pbas1_raw.decode("utf-8")

    pbas1_start = pbas1_raw.find("'") + 1
    pbas1_end = pbas1_raw.rfind("'")
    pbas1_str = pbas1_raw[pbas1_start:pbas1_end]

    if pbas1_str:
        pbas1 = list(pbas1_str)

    # Create the table with headers
    table = ["№ count\tDATA9\tDATA10\tDATA11\tDATA12\tPLOC1\tPBAS1"]

    # Determine the maximum length among the data lists
    max_length = max(len(data9), len(data10), len(data11), len(data12), len(ploc1))

    # Fill the table with data
    for i in range(max_length):
        row = [
            i + 1,
            data9[i] if i < len(data9) else "",
            data10[i] if i < len(data10) else "",
            data11[i] if i < len(data11) else "",
            data12[i] if i < len(data12) else "",
            "",
            ""
        ]

        # Check and insert data from PLOC1 and PBAS1
        if i + 1 in ploc1:
            index = ploc1.index(i + 1)
            row[5] = ploc1[index]
            if index < len(pbas1):
                row[6] = pbas1[index]
                del pbas1[index]
            del ploc1[index]

        table.append("\t".join(str(cell) for cell in row))

    # Save the table as a TXT file
    file_name = os.path.splitext(file_path)[0] + ".txt"
    with open(file_name, "w") as txtfile:
        txtfile.write("\n".join(table))

if __name__ == "__main__":
    # Process all files with the .ab1 extension in the current directory
    folder_path = os.getcwd()
    ab1_files = [f for f in os.listdir(folder_path) if f.endswith(".ab1")]

    for ab1_file in ab1_files:
        ab1_file_path = os.path.join(folder_path, ab1_file)
        
        # Checking if the filename is equal to 'file.txt' before calling the function
        if os.path.basename(ab1_file_path) == "file.ab1":
            convert_ab1_file_to_txt(ab1_file_path)