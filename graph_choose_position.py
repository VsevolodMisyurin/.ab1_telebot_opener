import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_position_electropherogram(start_ploc1, num_values_before, num_values_after, output_file):
    try:
        files_in_directory = os.listdir()
        txt_file = next((file for file in files_in_directory if file.endswith('.txt')), None)

        if txt_file:
            # Read data from .txt file using pandas
            df = pd.read_csv(txt_file, sep='\t', encoding='cp1251')
            ploc1_values = df['PLOC1'].dropna().tolist()

            # Find the central value of PLOC1
            central_ploc1 = ploc1_values[start_ploc1-1]

            # Find the central value index PLOC1
            central_ploc1_index = ploc1_values.index(central_ploc1)

            # Find the start and end values of PLOC1 for a range
            start_value_index = max(0, central_ploc1_index - num_values_before)
            end_value_index = min(len(ploc1_values), central_ploc1_index + num_values_after + 1)

            start_ploc1_value = ploc1_values[start_value_index]
            end_ploc1_value = ploc1_values[end_value_index - 1]

            # Find the minimum and maximum value of PLOC1 in the general table
            min_ploc1_value = min(start_ploc1_value, end_ploc1_value)
            max_ploc1_value = max(start_ploc1_value, end_ploc1_value)

            # Find the indexes of the rows containing value1 and value2 in column PLOC1
            start_index = df.index[df['PLOC1'] == min_ploc1_value].min()
            end_index = df.index[df['PLOC1'] == max_ploc1_value].max()

            # Cut DataFrame
            if start_index is not None and end_index is not None:
                df = df.loc[start_index:end_index]

            # Make a plot
            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df['DATA9'], label='DATA9', color='black')
            plt.plot(df.index, df['DATA10'], label='DATA10', color='green')
            plt.plot(df.index, df['DATA11'], label='DATA11', color='red')
            plt.plot(df.index, df['DATA12'], label='DATA12', color='blue')

            plt.xlabel('Nucleotides')
            plt.ylabel('Fluorescence intensity')
            plt.title('Electropherogram')

            # Get X-axis labels from PBAS1 column
            x_ticks = []
            x_labels = []
            for index, row in df.iterrows():
                if not pd.isna(row['PLOC1']):
                    x_ticks.append(index)
                    x_labels.append(row['PBAS1'])

            plt.legend()
            plt.xticks(x_ticks, x_labels)
            plt.savefig(output_file)
        else:
            print("No source files found in the current folder.")
    except Exception as e:
        print(f"An error has occurred: {e}")