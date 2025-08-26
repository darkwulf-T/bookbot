def count_words(file_string):
    words = file_string.split()
    count = len(words)
    return count

def count_characters(file_string):
    character_count = {}
    lower_string = file_string.lower()
    for character in lower_string:
        current = character_count.get(character,0)
        character_count[character] = current + 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_function(character_dic):
    sorted_list = []
    for char, num in character_dic.items():
        if char.isalpha():
            new_char_dict = {"char": char, "num": num}
            sorted_list.append(new_char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

