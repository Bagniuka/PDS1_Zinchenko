class TextProcessor:
    punctuation = ".,?!;:()'\""
    def get_clean_string(self, text):
        clean_text = ''
        for char in text:
            if self.__is_punctuation:
                continue
            clean_text += char
        return clean_text

    @classmethod
    def __is_punctuation(cls, char):
        return char in cls.punctuation

text = TextProcessor()
print(text.get_clean_string('asdf.sdf?mq!fqm,ffs:d;'))