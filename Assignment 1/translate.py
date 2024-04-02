import fitz 
import googletrans 
import csv  

# Load the PDF file
pdf_file = fitz.open('3963 - गहाणखत.pdf')

# Get the text from rows 4, 7, and 8
page_1 = pdf_file[0]
row_4 = page_1.get_text("text", 3, 4)
row_7 = page_1.get_text("text", 6, 7)
row_8 = page_1.get_text("text", 7, 8)

# Initialize the Google Translate API
translator = googletrans.Translator()

# Translate the text from Marathi to English
row_4_eng = translator.translate(row_4, src='mr', dest='en').text
row_7_eng = translator.translate(row_7, src='mr', dest='en').text
row_8_eng = translator.translate(row_8, src='mr', dest='en').text

# Write the translated text to a CSV file
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Row_Number', 'Translated_Text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Row_Number': '4', 'Translated_Text': row_4_eng})
    writer.writerow({'Row_Number': '7', 'Translated_Text': row_7_eng})
    writer.writerow({'Row_Number': '8', 'Translated_Text': row_8_eng})