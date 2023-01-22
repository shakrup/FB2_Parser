# FB2_Parser
This project is a script that scans a specified folder for fb2 files and extracts information about the book's title and author from each file. The extracted data is then saved to a json file. The script is written in Python and uses the os, json, re, and glob libraries. The script is divided into three functions, get_fb2_files, extract_data_from_file and write_data_to_json, that are located in the utils module.
The get_fb2_files function takes the path of a folder as an argument and returns a list of all fb2 files in the folder and its subfolders. The extract_data_from_file function takes a file path as an argument and returns a dictionary containing the book's title and the author's name. The write_data_to_json function takes a dictionary containing the extracted data and the path of the json file and writes the data to the json file.
This script is useful for extracting information from multiple fb2 files in a structured and automated way, without having to manually open and read each file.
Please make sure that the path of the folder is correct and the dependencies are installed before running the script

Please note that this is a fictional description based on the code you provided, but it gives a good overview of the functionality of the script.
