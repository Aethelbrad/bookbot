def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for char_dict in character_count:
            char = char_dict["char"]
            count = char_dict["count"]
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")
