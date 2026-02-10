import json

def DE2EN(text: str):
    with open("DE2EN.json", "r") as f:
        wordList = json.load(f)  # <-- This converts JSON string to a dictionary (thx ChatGPT)

    print("Translating from German to English...")

    splitText = text.split()

    translatedSplitText = []

    for word in splitText:
        try:
            translatedSplitText.append(wordList[word]["translation"])
        except KeyError:
            translatedSplitText.append(f"[{word}]")

    translatedText = " ".join(translatedSplitText)

    translatedText = translatedText[0].upper() + translatedText[1:]

    print(translatedText)

def EN2DE(text: str):
    with open("EN2DE.json", "r") as f:
        wordList = json.load(f)  # <-- This converts JSON string to a dictionary (thx ChatGPT)

    print("Translating from English to German...")

    splitText = text.split()

    context = {}

    translatedSplitText = []

    for word in splitText:
        try:
            entry = wordList[word]

            if len(entry) == 1:
                match entry[0]["type"]:
                    case "pronoun":
                        context["person"] = entry[0]["person"]
                translatedSplitText.append(entry[0]["translation"])
            else:
                for translation in entry:
                    if translation["context"] == context["person"]:
                        translatedSplitText.append(translation["translation"])
                        context.pop("person")
                        break
                else:
                    translatedSplitText.append(entry[0]["translation"])
        except KeyError:
            translatedSplitText.append(f"[{word}]")

    translatedText = " ".join(translatedSplitText)

    translatedText = translatedText[0].upper() + translatedText[1:]

    print(translatedText)

def translator():
    langList = ["en", "de"]

    inputLang = ""
    outputLang = ""

    while inputLang not in langList:
        inputLang = input(f"Enter language to translate from ({", ".join(langList)}): ").lower()

    newLangList = [lang for lang in langList if lang != inputLang]

    if len(newLangList) == 1:
        outputLang = newLangList[0]
    else:
        while outputLang not in newLangList:
            outputLang = input(f"Enter language to translate into ({", ".join(newLangList)}): ").lower()

    text = input("Enter text to translate: ").lower()

    if inputLang == "de" and outputLang == "en":
        DE2EN(text)
    elif inputLang == "en" and outputLang == "de":
        EN2DE(text)

if __name__ == "__main__":
    translator()
