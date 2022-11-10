from gtts import gTTS
import PyPDF2


file_path = input("What is the file path of the PDF you would like to convert?\n")
mp3_name = input("What would you like to name this mp3 file?\n")


text = []
try:
    with open(f"{file_path}", mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        for page in range(reader.getNumPages()):
            read_page = reader.getPage(page)
            page_text = read_page.extractText()
            text.append(page_text)

    text_body = "".join(text)
except FileNotFoundError:
    print("I'm sorry, but I didn't recognize that file path. Please double check and try again.")

else:
    print("\nYour PDF is being converted to an mp3. \nPlease wait a moment...")
    language = 'en'

    myobj = gTTS(text=text_body, lang=language, slow=False)

    if ".mp3" in mp3_name:
        mp3_name = mp3_name.replace(".mp3", "")
        myobj.save(f"{mp3_name}.mp3")
    else:
        myobj.save(f"{mp3_name}.mp3")

    print("\nYour PDF has been converted and saved in this directory. Have a wonderful day!")