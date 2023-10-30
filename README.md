# XML Data Parser

This Python script reads XML data from a file, parses it, and writes key-value pairs from the data to an Excel file.

## Dependencies

- **Python**: Make sure you have Python installed on your machine.
- **xml.etree.ElementTree**: This is part of Python's standard library and provides methods to parse XML files.
- **pandas**: This is a powerful data manipulation library that provides flexible data structures to manipulate and analyze data. You can install it using pip: `pip install pandas`.
- **openpyxl**: This is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files. You can install it using pip: `pip install openpyxl`.

## How to Run

1. Save the script in a .py file, for example, `xml_parser.py`.
2. Place your XML file (e.g., `xmsource.xml`) in the same directory as your Python script.
3. Open a terminal/command prompt.
4. Navigate to the directory containing your script and XML file.
5. Run the script using Python by typing `python xml_parser.py` and pressing Enter.

## Example Output

The script will create an Excel file named "tabula.xlsx" in the same directory as your Python script. The Excel file will have two columns: "Key" and "Value". Each row in the Excel file corresponds to a key-value pair from the XML data.

If you run the script again with the same filename, it will ask you whether you want to overwrite the existing file or append new data.

☠️
