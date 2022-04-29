import speech_recognition as sr

r = sr.Recognizer()


def s2t(audio_file: str):
    with sr.AudioFile(audio_file) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            with open("sample.txt", "w") as text_file:
                text_file.write(text)
            print("Successfully Created/Overwrote the file sample.txt")
        except:
            print('Sorry.. run again...')
            
