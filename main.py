from pypdf import PdfReader
import requests
import os

# Declare variables and get pdf file path.
text = ""
API_KEY = os.getenv("API_KEY")
pdf_path = input("Please enter your pdf path you want converted to an audiobook: ")

# Gather the text from the pdf file and store it all in the 'text' variable.
reader = PdfReader(pdf_path)
for i in range(len(reader.pages)):
    text += reader.pages[0].extract_text()

# Assign parameters and get audiobook from API.
parameters = {
    "key": API_KEY,
    "src": text,
    "hl": "en-us"
}
tts_response = requests.get("http://api.voicerss.org/", params=parameters)

# Put API result into audio file.
with open("output.mp3", "wb") as output_file:
    output_file.write(tts_response.content)
