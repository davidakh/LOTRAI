characters = {
    "frodo": "Frodo Baggins is a Hobbit and is 50 years old at the beginning of his journey. He is the Ringbearer and is present in all the Lord of the Rings books. Frodo was born in 1368 of the Shire Reckoning. Frodo leaves Middle Earth at the age of 53 to the Undying Lands.",
    "sam": "Samwise Gamgee is a Hobbit and Frodo's loyal companion.",
    "gollum": "Gollum, originally known as Sméagol, is a creature corrupted by the One Ring. He is pivotal in Frodo's journey.",
    "gandalf": "Gandalf is a Maia who takes the form of a wizard and plays a pivotal role in Middle-earth. Known as Gandalf the Grey and later Gandalf the White, he is a wise and powerful figure, guiding the Fellowship of the Ring in their quest to destroy the One Ring.",
    "aragorn": "Aragorn, also known as Strider, is a Dúnedain ranger and the rightful heir to the throne of Gondor. He is a skilled warrior, a leader of the Fellowship of the Ring, and plays a crucial role in the defeat of Sauron during the War of the Ring. Aragorn becomes King Elessar of the Reunited Kingdom at the end of the story.",
}

aliases = {
    "frodo baggins": "frodo",
    "samwise": "sam",
    "sam gamgee": "sam",
    "samwise gamgee": "sam",
    "sméagol": "gollum",
    "gollum": "gollum",
    "gandalf the grey": "gandalf",
    "gandalf the white": "gandalf",
    "mithrandir": "gandalf",
    "strider": "aragorn",
    "king elessar": "aragorn",
    "elessar": "aragorn"
}

# Combine canonical names and aliases into one lookup dictionary
all_names = {**aliases, **{name: name for name in characters}}

question = input("Ask about a LOTR character: ").lower()

# Extract character name from the question
character_name = next((all_names[word] for word in all_names if word in question), None)

if character_name:
    # Look up the character description
    print(characters[character_name])
else:
    print("No recognizable character found in your question. Please try again.")