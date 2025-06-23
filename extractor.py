import PyPDF2
import json
from field_mappings import field_mapping
from summary import get_summary


# === Helper: Clean field values ===
def clean_value(value):
    if isinstance(value, str):
        value = value.strip().strip("/").strip()
        if value.upper() == "YES":
            return "Yes"
        elif value.upper() == "NO":
            return "No"
    return value


# get clean addresses of the company and the auditor
def clean_address(output):

    auditor_address = ", ".join(
        filter(
            None,
            [
                output.pop("auditor_address_line1", ""),
                output.pop("auditor_address_line2", ""),
                output.get("auditor_city", ""),
                output.get("auditor_state", ""),
                output.get("auditor_pin", ""),
            ],
        )
    )
    if auditor_address:
        output["auditor_address"] = auditor_address
    company_addr = output.get("registered_office")
    if not isinstance(company_addr, str):
        return output
    cleaned = company_addr.replace("\r", ", ").replace("\n", ", ")
    cleaned = ", ".join(
        part.strip() for part in cleaned.split(",") if part.strip()
    )  # noqa
    output["registered_office"] = cleaned
    return output


# Extractor function
def extract_form_values(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        if not reader.get_fields():
            return {}
        form_fields = reader.get_fields()
        field_values = {}
        for field_name, field_data in form_fields.items():
            field_values[field_name] = field_data.get("/V", "")
        return field_values


#  Main Execution
path = "Form_ADT-1-29092023_signed.pdf"
form_values = extract_form_values(path)
output = {}

for field, value in form_values.items():
    simple_name = field.split(".")[-1].split("[")[0].lower()
    if simple_name in ["signature", "sig", "signed", "sign1", "sign_stp"]:
        continue
    mapped_key = field_mapping.get(simple_name)
    if mapped_key:
        output[mapped_key] = clean_value(value)

# get clean address
output = clean_address(output)

# Output to JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

# get summary

summary = get_summary(output)
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)
