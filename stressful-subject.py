def remove_repeated_letters(subj):
    characters = []
    for index in range(len(subj)):
        if subj[index] != subj[index-1]:
            characters.append(subj[index])
    return characters

def remove_non_letters(characters):
    letters_list = []
    for character in characters:
        if character.isalpha() or character == " ":
            letters_list.append(character.lower())
    letters = "".join(letters_list)
    return letters

def find_red_words(letters):
    red_words = ["help", "asap", "urgent"]
    for word in letters.split():
        if word in red_words:
            return True

def is_stressful(subj):
    if find_red_words(remove_non_letters(remove_repeated_letters(subj))):
        return True
    elif subj.isupper():
        return True
    elif subj.endswith("!!!"):
        return True
    else:
        return False
