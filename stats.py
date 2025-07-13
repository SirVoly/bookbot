def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dictionary = {}

    for character in text.lower():
        if character not in character_dictionary:
            character_dictionary[character] = 0
        character_dictionary[character] += 1

    return character_dictionary

def sort_characters(character_dictionary):
    # create list
    character_list = []
    for key in character_dictionary:
        character_list.append({
            "char":key,
            "num":character_dictionary[key]
        })

    # sort function
    def sort_on(items):
        return items["num"]

    # sort list
    character_list.sort(reverse=True, key=sort_on)
    return character_list
