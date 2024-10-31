# Задание №3
from translate import Translator
import requests
from collections import defaultdict

# Задание №5
qwestions = {'как тебя зовут' : "я бот, созданый чтобы переводить твои сообщения!",
             "сколько тебе лет" : "достаточно",
             "почему перевод такой кривой?": "потому что я плохо знаю английский",
             "i put the new forgis on the jeep": "i trap until bloody bottoms is underneath",
             "как дела?": "нормально, у меня их нет :)",
             "у тебя есть планы по захвату мира?": "пока нету... пока нету...",
             "привет": "здравствуй!",
             "что ты любишь?": "я любюлю переводить текст, так что давай переведём что-нибудь!"}

class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)

    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text.lower() in qwestions.keys():
            self.response = qwestions[text]
        else:
            self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("я не понял тебя", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang=from_lang, to_lang=to_lang)

            translation = translator.translate(text)
            return translation 
        except:
            return "Перевод не удался"