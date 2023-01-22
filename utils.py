import os
import json
import re
import glob

# Function to get all the fb2 files from the specified folder and its subfolders
def get_fb2_files(folder_path):
    # Change the current working directory to the specified folder
    os.chdir(folder_path)
    # Use glob to search for all files ending in '.fb2' in the folder and its subfolders
    return glob.glob(os.path.join(folder_path, '**', '*.fb2'), recursive=True)

# Function to extract data from a given file
def extract_data_from_file(file):
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as file_name:
            # Read the contents of the file
            stroke = file_name.read()
            # Convert the contents to a string
            stroke = str(stroke)
            # Regular expressions to find the book title, author's last name, and author's first name
            reg_title = '<book-title>(.+?)</book-title>'
            reg_last_name = '<last-name>(.+?)</last-name>'
            reg_first_name = '<first-name>(.+?)</first-name>'
            title = re.findall(reg_title, stroke)
            last_name = re.findall(reg_last_name, stroke)
            first_name = re.findall(reg_first_name, stroke)
            if len(title) > 0:
                title = str(title)
            else:
                title = "N/A"
            if len(first_name) > 0:
                author = last_name[0] + ' ' + first_name[0]
            elif len(last_name) > 0:
                author = last_name[0]
            else:
                author = "N/A"
                title = "N/A"
            # Return the extracted data as a dictionary
            return {"Author": author, "Title": title}
    except IndexError:
        print("Error with file", file)
        return None

# Function to write data to a json file
def write_data_to_json(data, json_file):
    # Open the json file and write the data to it
    with open(json_file, 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
