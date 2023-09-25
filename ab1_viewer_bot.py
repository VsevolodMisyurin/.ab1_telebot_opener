import telebot
import os
from ab1_processor import process_ab1_file
from get_native_txt_table_GATC import convert_ab1_file_to_txt
from graph_choose_position import generate_position_electropherogram
from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Create a state to track user selection
user_states = {}
command_message = "To get an electropherogram press /picture.\nTo get the sequence press /sequence.\nTo receive the sequence in fasta format press /fasta.\nTo make a close view from position - press /close_view."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a bot that helps you open and view .ab1 files. Upload your .ab1 file here.")

# File upload handler
@bot.message_handler(content_types=['document'])
def get_ab1_file(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Save the file with the extension .ab1
        with open("file.ab1", 'wb') as new_file:
            new_file.write(downloaded_file)
        
        # Convert the uploaded .ab1 file and obtain the .txt file for /close_view
        sequence = convert_ab1_file_to_txt("file.ab1")
        if sequence:
            bot.reply_to(message, f"Your file uploaded and processed. {command_message}")
        else:
            bot.reply_to(message, f"Your file uploaded and processed. {command_message}")
        
        # Set user state to await command
        user_states[message.chat.id] = 'waiting_command'
    except Exception as e:
        bot.reply_to(message, f"Failed to process file format .ab1 38 line")


# Handler for processing commands after loading a file
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_command')
def handle_commands(message):
    if message.text == '/sequence':
        # Process the file and obtain the genetic sequence
        sequence = process_ab1_file("file.ab1")
        if sequence:
            bot.reply_to(message, f"{sequence}")
        else:
            bot.reply_to(message, "Failed to process file format .ab1, 50 line")
        bot.reply_to(message, command_message)
    elif message.text == '/picture':
        # Process the .ab1 file and send the electrophorogram
        generate_electropherogram(message.chat.id)
        bot.reply_to(message, f"{sequence}")
    elif message.text == '/fasta':
        # Process the file and send the sequence in FASTA format
        sequence, file_name = get_sequence_and_filename("file.ab1")
        if sequence:
            reply_message = f"> {file_name}, {len(sequence)} bases\n{sequence}"
            bot.reply_to(message, reply_message)
        else:
            bot.reply_to(message, "Failed to process file format .ab1, 61 line")
        bot.reply_to(message, command_message)
    elif message.text == '/close_view':
        # Process the .txt file and send the electrophorogram
        user_states[message.chat.id] = 'waiting_number'
        bot.reply_to(message, "Please enter a number:")
        bot.reply_to(message, f"{sequence}")
    else:
        bot.reply_to(message, command_message)

def handle_close_view(chat_id):
    try:
        os.system("graph_choose_position.py")

        # Sends an image with an electrophorogram
        image_path = "electropherogram_file.ab1.png"
        with open(image_path, "rb") as photo:
            bot.send_photo(chat_id, photo)
    except Exception as e:
        bot.send_message(chat_id, f"An error has occurred: {e}")


def generate_electropherogram(chat_id):
    try:
        # Calls code from electropherogram_generator.py to generate an electropherogram
        os.system("python electropherogram_generator.py")

        # Sends an image with an electrophorogram
        image_path = "electropherogram_file.ab1.png"
        with open(image_path, "rb") as photo:
            bot.send_photo(chat_id, photo)

    except Exception as e:
        bot.send_message(chat_id, f"An error has occurred: {e}")

# Function to obtain sequence and file name
def get_sequence_and_filename(file_path):
    try:
        # Process the file and obtain the genetic sequence
        sequence = process_ab1_file(file_path)
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        return sequence, file_name
    except Exception as e:
        return None, str(e)

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_number')
def handle_number_input(message):
    try:
        # Get the number entered by the user
        number = int(message.text)

        # Call the generate_position_electropherogram function with the necessary values
        generate_position_electropherogram(number, 12, 12, 'chosen_electropherogram.png')

        # Send the file to the user
        with open('chosen_electropherogram.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        # Reset the user's state back to waiting for a command
        user_states[message.chat.id] = 'waiting_command'
    except ValueError:
        # If the user entered a non-number, inform them about the error
        bot.reply_to(message, "Please enter a valid number.")

if __name__ == "__main__":
    bot.infinity_polling()
