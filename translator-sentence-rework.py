import json
import re

def DE2EN(text: str, wordList: dict):
    return

def EN2DE(text: str, wordList: dict):
    return

def split_sentences(input: str) -> list:
    return # Warning: Hard to implement

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

    splitInput = split_sentences(text)

    if inputLang == "de" and outputLang == "en":
        with open("DE2EN.json", "r") as f:
            wordList = json.load(f)  # <-- This converts JSON string to a dictionary (thx ChatGPT)

        output = ""
        for sentence in splitInput:
            output += DE2EN(sentence, wordList)
        return output
    elif inputLang == "en" and outputLang == "de":
        with open("EN2DE.json", "r") as f:
            wordList = json.load(f)  # <-- This converts JSON string to a dictionary (thx ChatGPT)

        output = ""
        for sentence in splitInput:
            output += EN2DE(sentence, wordList)
        return output

if __name__ == "__main__":
    output = translator()
    print(output)
