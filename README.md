# ADT-1 Extraction

This project extracts structured data from filled and signed ADT-1 PDF forms using Python. It maps PDF form fields to standardized JSON keys for further processing or record-keeping.

## Features

- Extracts data from ADT-1 PDF forms using `PyPDF2`
- Maps PDF field names to standardized output fields
- Cleans and formats addresses and other field values
- Outputs extracted data as a JSON file (`output.json`)

## Requirements

- Python 3.8+
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. Clone this repository:
   ```sh
   git clone <your-repo-url>
   cd ADT-1-extraction
   ```
2. Install dependencies:
   ```sh
   pip install PyPDF2
   ```

## Usage

1. Place your filled and signed ADT-1 PDF file in the project directory (default: `Form_ADT-1-29092023_signed.pdf`).
2. Run the extractor:
   ```sh
   python extractor.py
   ```
3. The extracted data will be saved to `output.json`.

## File Structure

- `extractor.py`: Main script for extracting and processing PDF form data.
- `field_mappings.py`: Maps PDF field names to output JSON keys.
- `Form_ADT-1-29092023_signed.pdf`: Example input PDF form.
- `output.json`: Output file containing extracted data.
- `README.md`: Project documentation.

## Customization

- To use a different PDF file, change the `path` variable in `extractor.py`.
- Update `field_mappings.py` to adjust field mappings as needed.
