# .ab1_telebot_opener
This Telegram bot is designed to assist researchers in processing their .ab1 file format. You can upload the file to the chat and receive information about the read DNA sequence as a string and in FASTA format, and obtain an electropherogram. You can also get a 12se pair fragment of the electropherogram on both sides of the user-selected base.


[How to use](#How_to_use)

[Installation](#Installation)

[Launching](#Launching)

[Limitations](#Limitations)

<a name="How to use"></a> 
**How to use**

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/b4d36e7f-0367-4885-be55-cba85e6e6901)
By clicking on the link in the chat, press the 'Start' button.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/f0d77437-6b95-4565-91e6-1a87882df08e)
After that, you will see a greeting inviting you to upload a .ab1 file. Simply drag and drop your file into the chat or click on the "attachment" icon to specify the upload path.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/44076aed-0ac5-4411-b438-2f7d64fbfa4e)
When your file is fully uploaded, the bot will notify you and offer several functions. By typing /sequence, you can get the sequenced DNA sequence and insert it, for example, into your report. By typing /fasta, you can also get the sequenced DNA sequence in FASTA format, which includes the sequence's length and the actual sequence itself. By typing /picture, you can obtain the electropherogram of the entire sequence, from the first to the last letter. The overall view of the electropherogram allows you to assess the quality of the sequencing. By typing /close_view, you can also assess any specific fragment of the read DNA that interests you.

I will provide some examples of how it works
![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/80c69fa6-dfa1-44a4-a251-033ad2a862ad)
The entire DNA sequence will be presented after selecting the /sequence command.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/93f8054d-ed5d-40be-a253-54fd524ce7ac)
This is the format of FASTA that you can obtain after pressing the /fasta button.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/29b36a65-176e-4bd2-a582-9a7fd78cf19c)
The electropherogram obtained after pressing the /picture button may take around 5-10 seconds to generate, depending on the length of the reading. Due to the long length of the sequenced sequence, all nucleotides may appear as a single black line.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/3beec6eb-0b42-4dd2-b39d-7d141752e090)
When you press /close_view, the bot will ask you to enter the position you're interested in. You provided the number 375 as an example. After entering the number, the bot will show you an electropherogram with the nucleotide at position 375 (or the one you entered) in the sequenced sequence at the center. The electropherogram will be displayed from 12 nucleotides before the one you selected to 12 nucleotides after it.

The default position is set to "12". You can change it by entering your desired numbers in line 117 of the ab1_viewer_bot.py file.

I can provide examples for different readings if needed.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/d7958af5-486a-45d1-a607-ad5e58ba746b)
A high-quality sequence typically looks something like this.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/96139db6-91da-4d6d-8949-ced2993a94ab)
Upon closer examination, it can be seen that capillary electrophoresis was performed cleanly, without any interference or contamination.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/8b2952ae-6643-42ee-8a3b-27221d11467f)
In the new example, the sequence has poor quality.

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/baf77d63-c7ed-411f-8168-7080cc9809e1)
Upon closer inspection, numerous reading artifacts are visible, which is typical for low-quality sequences.

<a name="Installation"></a>
**Installation**

To work, you need to have Python installed, as well as the libraries telebot, biopython, matplotlib.pyplot, and pandas.
You can install Python from here: https://www.python.org/downloads/. Install version 3.8, as the bot works stably with this version.
You also need to install Telebot from https://pypi.org/project/pyTelegramBotAPI/. Install the latest version using the instructions on that page.
After installation, download the necessary libraries using the following commands:

pip install biopython
pip install matplotlib
pip install pandas

Next, simply copy all the files from this repository into one folder on your computer. It's crucial that all files with the .py extension are in the same directory, as the main file ab1_viewer_bot.py looks for other files in the same directory where it's located.
Remove example.ab1 from folder.
Don't forget to record the token number you received when creating the Telegram bot in the config.py file.


<a name="Launching"></a>
**Launching**

![image](https://github.com/VsevolodMisyurin/.ab1_telebot_opener/assets/111582251/b59c4172-c8e5-4fc7-b6ac-016f94c05770)
For convenient execution, you can open the folder containing the bot's components. Right-click in the address bar to highlight the address, type "cmd," and the command prompt will open.
After opening the command prompt, enter the following command:
python ab1_viewer_bot.py
Then open the Telegram bot in Telegram and proceed with the analysis!


<a name="Limitations"></a>
**Limitations**

Unfortunately, the bot does not keep a file history and always works with the latest .ab1 file. When a new file is uploaded, the old file gets overwritten. It is not possible to have multiple users working simultaneously.
