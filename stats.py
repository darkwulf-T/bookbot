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
