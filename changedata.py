import os
import re

def replace_first_number_in_line(line):
    # Replace the first occurrence of a digit in each line with 0
    return re.sub(r'(\D*)(\d)', lambda match: match.group(0).replace(match.group(2), '0', 1), line, count=1)

def replace_first_number_in_file(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        new_lines = [replace_first_number_in_line(line) for line in lines]

        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Overwrite the file with the new lines
        file.writelines(new_lines)
        # Truncate the file to the new size (in case new content is shorter)
        file.truncate()

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path) and os.path.getsize(file_path) > 0: # Ensure the file is not empty
                replace_first_number_in_file(file_path)

# Replace 'your_directory_path' with the actual path to the directory you want to process
process_directory('/Users/visea/DataspellProjects/YoloTrainer/datasets/haimian/train/labels')