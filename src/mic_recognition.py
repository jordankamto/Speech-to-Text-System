import speech_recognition as sr

rec_vocale = sr.Recognizer()
mic = sr.Microphone()

with mic as src:
   rec_vocale.adjust_for_ambient_noise(src)
   while True:
     audio = rec_vocale.listen(src)
     texte = rec_vocale.recognize_google(audio, language=fichier[1]) # Traduction
     print(texte)
