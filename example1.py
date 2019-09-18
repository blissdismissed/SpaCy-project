from spacy.lang.de import German

nlp = German()

doc = nlp("Liebe Grüsse!")

print(doc.text)


