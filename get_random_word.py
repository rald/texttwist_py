import random

def get_random_word(file_path="wordlist.txt"):
    """Reads a wordlist file and returns a random word."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]

        if not words:
            raise ValueError("The wordlist file is empty.")

        return random.choice(words)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError as e:
        print(e)
        return None

# Example usage:
# word = get_random_word("my_words.txt")
# print(word)

word = get_random_word("rndwords.txt")
print(word)
