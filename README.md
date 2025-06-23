# ADT-1 Extraction

This project extracts structured data from ADT-1 PDF forms, maps the fields to meaningful names, cleans the data, and generates both a JSON output and a human-readable summary.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MahtabTanim/ADT-1-extraction.git
   cd ADT-1-extraction
   ```

2. **Install dependencies:**

   ```bash
   pip install pypdf2 cohere pymupdf pytesseract pillow
   ```

   - `pypdf2` is used for PDF form extraction.
   - `cohere` is used for AI-powered summary generation (if enabled).
   - `pymupdf` (imported as `fitz`) is used for extracting embedded attachments from PDFs.
   - `pytesseract` and `pillow` are used for OCR on scanned PDF pages.

3. **(Optional) Install any other dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   If you add more dependencies, update `requirements.txt` accordingly.

## File Overview

- **extractor.py**
  Main script. Extracts data from the ADT-1 PDF, cleans and maps fields, writes output to JSON, and generates a summary.

- **field_mappings.py**
  Contains the mapping between raw PDF field names and user-friendly keys used in the output.

- **summary.py**
  Contains the function to generate a human-readable summary from the structured data (optionally using an AI model).

- **attachment_extraction.py**
  Extracts embedded attachments from the ADT-1 PDF, saves them, and extracts text from each attachment (including OCR for scanned PDFs).

- **output.json**
  The structured data extracted from the PDF, saved as JSON.

- **summary.txt**
  The AI-generated, human-readable summary of the filing.

## Usage

1. **Place your ADT-1 PDF file** in the project directory and update the `path` variable in `extractor.py` if needed.

2. **Run the extractor:**

   ```bash
   python extractor.py
   ```

3. **Outputs:**
   - `output.json`: Structured extracted data.
   - `summary.txt`: Human-readable summary of the filing.
   - `attachments/`: Folder containing extracted attachments from the PDF.

## Customization

- **Field Mappings:**
  Update `field_mappings.py` to map additional or custom PDF fields.
- **Summary Generation:**
  Edit `summary.py` to change the style or content of the summary.

## Example Output

**output.json**

```json
{
    "company_name": "ALUPA FOODS PRIVATE LIMITED",
    "auditor_name": "MALLYA & MALLYA",
    "appointment_date": "29/08/2022",
    ...
}
```

**summary.txt**

```
ALUPA FOODS PRIVATE LIMITED has appointed MALLYA & MALLYA as its statutory auditor for FY 2022–2027, effective from 29/08/2022.
The appointment has been disclosed via Form ADT-1,
with all supporting documents submitted.
```

---

## Attachment Extraction

> **Note:**
> For attachment extraction, please switch to the `attachment_extraction` branch for the latest features and fixes related to extracting and processing embedded files.

### How it works

- **attachment_extraction.py** will:

  - Scan the original PDF for attachments , extract the texts .

  - The function `get_attachment_texts()` returns a list of extracted texts from all successfully processed attachments.

---

## Notes

- Ensure your PDF is a digitally filled ADT-1 form with extractable fields.
- For best results, use clear, machine-readable PDFs.
- **For the sake of testing, the API key used in this project is public.**
  Please do not use this key for production or sensitive data, and rotate it if you fork or reuse this code.

---
