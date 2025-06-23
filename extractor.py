import PyPDF2
from PyPDF2 import PdfReader

path = "./Form_ADT-1-29092023_signed.pdf"
pdf = open(path, "rb")
reader = PyPDF2.PdfReader(pdf)
# info = reader.metadata
# print(len(reader.pages))
# print(reader.pages[0].extract_text())
# results = []


# for i in range(0, len(reader.pages)):
#     text = reader.pages[i].extract_text()
#     results.append((text))
def extract_form_values(path):
    with open(path, "rb") as file:
        if not reader.get_fields():
            return
        form_fields = reader.get_fields()
        field_values = {}
        for field_name, field_data in form_fields.items():
            field_values[field_name] = field_data.get("/V", None)

        return field_values


results = ""
form_values = extract_form_values(path)
for field, value in form_values.items():
    simple_name = field.split(".")[-1].split("[")[0]
    if simple_name.lower() in ["signature", "sig", "signed", "sign1", "sign_stp"]:
        continue
    results += f"{simple_name}  : {value}\n"
with open("form_values.txt", "w", encoding="utf-8") as f:
    f.write(results)

pdf.close()
