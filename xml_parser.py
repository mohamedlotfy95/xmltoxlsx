# Import the required libraries
import xml.etree.ElementTree as ET
import pandas as pd
import os

# Function to read XML data from a file
def read_xml_file(file_path):
    """Reads an XML file and returns its content."""
    with open(file_path, 'r') as file:
        return file.read()

# Function to parse XML data
def parse_xml_data(xml_data):
    """Parses XML data and returns the root element."""
    return ET.fromstring(xml_data)

# Function to get key-value pairs from the XML data
def get_key_value_pairs(root):
    """Extracts key-value pairs from the XML data and returns them as a list."""
    data = []
    for elem in root.iter('add'):
        data.append([elem.attrib['key'], elem.attrib['value']])
    return data

# Function to write data to an Excel file
def write_to_excel(data, file_name):
    """Writes data to an Excel file. If the file already exists, asks the user whether to overwrite or append."""
    df = pd.DataFrame(data, columns=['Key', 'Value'])
    
    if os.path.exists(file_name):
        print(f"'{file_name}' already exists.")
        choice = input("Enter 'O' to overwrite or 'A' to append: ").upper()
        
        if choice == 'O':
            df.to_excel(file_name, index=False)
            print(f"Data has been written to '{file_name}'.")
        elif choice == 'A':
            df_old = pd.read_excel(file_name)
            df_new = pd.concat([df_old, df])
            df_new.to_excel(file_name, index=False)
            print(f"Data has been appended to '{file_name}'.")
        else:
            print("Invalid choice. No data has been written.")
    else:
        df.to_excel(file_name, index=False)
        print(f"Data has been written to '{file_name}'.")

# Main function to orchestrate the execution of the script
def main():
    """Main function that orchestrates the reading, parsing, and writing operations."""
    xml_data = read_xml_file('xmsource.xml')
    root = parse_xml_data(xml_data)
    data = get_key_value_pairs(root)
    write_to_excel(data, 'tabular.xlsx')

if __name__ == "__main__":
    main()
