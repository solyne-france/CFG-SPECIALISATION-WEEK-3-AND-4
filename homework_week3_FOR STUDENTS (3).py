"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


#def generate_phrase(characters, phrase):
  #  pass
ef generate_phrase(characters, phrase):
    character_list = []
    phrase_characters = []
    characters = characters
    characters_no_space = characters.replace(" ", "")
    characters_lower = characters_no_space.lower() 
    phrase = phrase
    phrase_no_space = phrase.replace(" ", "") 
    phrase_lower = phrase_no_space.lower()  
    if len(characters) >= len(phrase):
        for character in phrase_lower:
            if character in characters_lower:
            character_list.append(character)
        for letter in phrase_lower:
          
            phrase_characters.append(letter)
    elif len(characters) < len(phrase):
        print("not enough characters for that phrase")
        return False
    if character_list == phrase_characters:
        print(f"the word {phrase} characters: {characters}")
        return True
    else:
        print("Sorry the phrase not available")
        return False





def generate_phrase():
    character_list = []
    phrase_characters = []
    characters = input("Please enter your characters: ")
    characters_no_space = characters.replace(" ", "") 
    phrase = input("Please enter your phrase: ")
    phrase_no_space = phrase.replace(" ", "")
    phrase_lower = phrase_no_space.lower()  
    if len(characters) >= len(phrase):
        for character in phrase_lower:
            if character in characters_lower:
    
                character_list.append(character)
        for letter in phrase_lower:
        
            phrase_characters.append(letter)
    elif len(characters) < len(phrase):
        print("Sorry there are not enough characters for that phrase")
        return False
    if character_list == phrase_characters:
        print(f"write the word{phrase} characters: {characters}")
        return True
    else:
        print("Sorrythe phrase not available")
        return False


