from googletrans import Translator

translator = Translator()
translation = translator.translate("Bonjour tout le monde", dest='en')
print(translation.text)
