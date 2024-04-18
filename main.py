meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict:
    meaning = meme_dict[word]
    print(f"{word} kelimesi şu anlama gelir: {meaning}")
else:
    print("Bu kelimenin anlamını bilmiyorum.")
