from docx import Document
doc = Document("plantilla.docx")

for p in doc.paragraphs:
    if "{{NOMBRE}}" in p.text:
        p.text = p.text.replace("{{NOMBRE}}", "Jordi Bosch")

doc.save("plantilla-edited.docx")