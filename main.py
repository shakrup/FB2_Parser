import os
# Import the functions from the utils module
from utils import get_fb2_files, extract_data_from_file, write_data_to_json

# The path of the folder containing the fb2 files
folder_path = 'C:\\BOOKS\\'

# Check if the folder exists
if not os.path.exists(folder_path):
    print("Error: Folder not found at {}".format(folder_path))
else:
    # Get a list of all the fb2 files in the folder and its subfolders
    fb2_files = get_fb2_files(folder_path)
    print('Scanning folder:', folder_path)
    print('Found', len(fb2_files), 'fb2 files')

    # Initialize an empty dictionary to store the extracted data
    data = {}

    # Iterate through each file
    for file in fb2_files:
        print('Processing file:', file)
        # Extract data from the file
        file_data = extract_data_from_file(file)
        if file_data:
            # Add the file data to the dictionary
            data[file] = file_data

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path of the json file
    json_file = os.path.join(script_dir, 'fb2_data.json')
    # Write the data to the json file
    write_data_to_json(data, json_file)
