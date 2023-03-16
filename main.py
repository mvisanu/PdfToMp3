import pyttsx3

from pypdf import PdfReader

pdfreader = PyPDF2.PdfReader(open('ChatGPT_Cheatsheet_Costa.pdf', 'rb'))
speaker = pyttsx3.init()



reader = PdfReader("ChatGPT_Cheatsheet_Costa.pdf")
text = ""
for page in reader.pages:
    text = page.extract_text() 
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'chatgpt.mp3')
speaker.runAndWait()

speaker.stop()