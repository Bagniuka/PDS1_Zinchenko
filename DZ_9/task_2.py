class TextProcessor:
    punctuation = ".,?!;:()'\"*/\\[]{}#@%&"

    @classmethod
    def __is_punctuation(cls, char):
        return char in cls.punctuation

    def get_clean_string(self, text):
        clean_text = ''
        for char in text:
            if self.__is_punctuation(char):
                continue
            clean_text += char
        return clean_text


class TextLoader:
    __text_processor = TextProcessor()
    __clean_string = None

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_stirng(self):
        print(f"Очищений текст: {self.__clean_string}")
        return self.__clean_string


class DataInterface:
    __text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_text(text)
            clean = self.__text_loader.clean_stirng
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
text = ["My, name is? Rost'yslav!", "I,am lear\"ning. Py!th!on"]
di.process_texts(text)
