import fitz  # PyMuPDF
import os
import json
import pytesseract
from PIL import Image
import io

pdf_path = "Form_ADT-1-29092023_signed.pdf"
output_dir = "attachments"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
attachment_count = doc.embfile_count()

print(f"Found {attachment_count} embedded file(s)")

extracted_data = []


# extract each attachments texts
def extract_text_from_pdf(file_path, file_name):
    try:
        with fitz.open(file_path) as embedded_doc:
            full_text = ""
            for page in embedded_doc:
                # Extract normal text
                text = page.get_text("text").strip()

                if not text:
                    # If no text, do OCR
                    pix = page.get_pixmap(dpi=300)
                    img = Image.open(io.BytesIO(pix.tobytes()))
                    ocr_text = pytesseract.image_to_string(img).strip()
                    full_text += ocr_text + "\n"
                else:
                    full_text += text + "\n"

        extracted_data.append(full_text.strip())

    except Exception as e:
        print(f"Failed to extract text from {file_name}: {e}")


# Extract + process each attachment
for i in range(attachment_count):
    try:
        file_data = doc.embfile_get(i)
        file_name = f"attachment_{i + 1}.pdf"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "wb") as f:
            f.write(file_data)
        extract_text_from_pdf(file_path, file_name)

    except Exception as e:
        print(f"Skipped attachment #{i + 1}: {e}")
        continue

doc.close()


def get_attachment_texts():
    return extracted_data
