import spacy
# Download and install the 'en_core_web_sm' model
# spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

def extract_locations_from_text(user_input):
    doc = nlp(user_input)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return locations
print(extract_locations_from_text("Hello from ahmedabad and mumbai delhi, new york"))