import random

templates = [
    "It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun3}!",
    
    "This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun}. I am so {feeling1} to {verb} in a tent. I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number} {measure_of_time}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!",
    
    "Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {creature_plural1} and {adjective3} {creature_plural2} here! In the {room} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {plural_noun3} and dream of {adjective4} {plural_noun4}. It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"
]

def get_input(prompt):
    while True:
        user_input = input(prompt + ": ").strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def generate_story(template):
    try:
        inputs = {
            "number": get_input("Type a number"),
            "measure_of_time": get_input("Type a measure of time"),
            "mode_of_transportation": get_input("Type a mode of transportation"),
            "adjective": get_input("Type an adjective"),
            "adjective2": get_input("Type another adjective"),
            "noun": get_input("Type a noun"),
            "color": get_input("Type a color"),
            "body_part": get_input("Type a part of the body"),
            "verb": get_input("Type a verb"),
            "number2": get_input("Type another number"),
            "noun2": get_input("Type another noun"),
            "noun3": get_input("Type one more noun"),
            "body_part2": get_input("Type another part of the body"),
            "verb2": get_input("Type another verb"),
            "noun4": get_input("Type a final noun"),
            "adjective3": get_input("Type another adjective"),
            "silly_word": get_input("Type a silly word"),
            "person_name": get_input("Type a person’s name"),
            "feeling1": get_input("Type a feeling"),
            "feeling2": get_input("Type another feeling"),
            "animal": get_input("Type an animal"),
            "verb2": get_input("Type another verb"),
            "color2": get_input("Type another color"),
            "adverb": get_input("Type an adverb"),
            "animal2": get_input("Type another animal"),
            "silly_word": get_input("Type a silly word"),
            "place": get_input("Type a place"),
            "creature_plural1": get_input("Type a magical creature (plural)"),
            "creature_plural2": get_input("Type another magical creature (plural)"),
            "room": get_input("Type a room in a house"),
            "plural_noun3": get_input("Type a plural noun"),
            "adjective4": get_input("Type another adjective"),
            "plural_noun4": get_input("Type another plural noun"),
            "verb_ing": get_input("Type a verb ending in 'ing'"),
            "adjective5": get_input("Type another adjective"),
            "noun5": get_input("Type another noun")
        }
        story = template.format(**inputs)
        print("\nGenerated Story:\n", story)
    except KeyError as e:
        print(f"Error: Missing input for {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

template_choice = int(get_input("Choose a template (1, 2, or 3)")) - 1
if 0 <= template_choice < len(templates):
    generate_story(templates[template_choice])
else:
    print("Invalid choice. Please restart and choose a valid template number.")
