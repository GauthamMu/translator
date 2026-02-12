import json

def DE2EN(text: str, wordList: dict):
    return

def EN2DE(text: str, wordList: dict):
    return

def split_sentences(text: str) -> list: # Not complete (have to add multiple punctuation support)
    sentences = [["", ""], ]

    for position, character in enumerate(text):
        if character in ".?!" and (position + 1 == len(text) or text[position+1] == " "):
            sentences[-1][1] = character
            sentences.append(["", ""])
        else:
            sentences[-1][0] += character

    return sentences

def translator():
    # Supported languages
    langList = ["en", "de"]

    inputLang = ""
    outputLang = ""

    # Ask user for input language until valid
    while inputLang not in langList:
        inputLang = input(f"Enter language to translate from ({", ".join(langList)}): ").lower()

    newLangList = [lang for lang in langList if lang != inputLang]

    # Determine output language; only prompt if multiple options
    if len(newLangList) == 1:
        outputLang = newLangList[0]
    else:
        while outputLang not in newLangList:
            outputLang = input(f"Enter language to translate into ({", ".join(newLangList)}): ").lower()

    text = input("Enter text to translate: ").lower()

    splitInput = split_sentences(text)

    # Yes, the following code is WET. Deal with it. clarity > cleverness
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
