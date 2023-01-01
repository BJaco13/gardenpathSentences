import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
                        'The old man the boat.',
                        'The complex houses married and single soldiers and their families.',
                        'The horse raced past the barn fell.',
                        'The florist sent the flowers was pleased.',
                        'The sour drink from the ocean.',
                        'The Cape Town International Airport'
                        ]

for item in gardenpathSentences:

    sentence = nlp(item)

    sentence.text.split()

    #print([(w.text, w.pos_) for w in sentence])

    print([token.orth_ for token in sentence if not token.is_punct | token.is_space])

    sentence2 = nlp(item)
    print([(i, i.label_, i.label) for i in sentence2.ents])

entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")

entity_fac = spacy.explain("ORG")
print(f"ORG:{entity_fac}")


# ===== Entity lookup ===== #

# Nr.1 - India:
# Yes, it was given under GPE (Countries, Cities, States)

# Nr.2 - Cape Town International Airport:
# No, it was given under ORG (Companies, Agencies, Institutions)