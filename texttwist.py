import random



def load_words(filename='words.txt'):
	words=[]
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			w = line.strip().lower()
			if w:
				words.append(w)
	return words



def get_anagrams(word, words):
    target_lower = word.lower()
    target_len = len(target_lower)

    # 1. Build an array-based frequency map for the target (size 26 for 'a'-'z')
    target_counts = [0] * 26
    for char in target_lower:
        target_counts[ord(char) - 97] += 1

    results = []

    # 2. Fast scan through cached words
    for candidate in words:
        cand_len = len(candidate)
        # Pre-filter by length (must be between 3 and target length)
        if cand_len < 3 or cand_len > target_len:
            continue

        # Fast subset check using list copy and array indexing
        counts = list(target_counts)
        valid = True
        for char in candidate:
            idx = ord(char) - 97
            if counts[idx] == 0:
                valid = False
                break
            counts[idx] -= 1

        if valid:
            results.append(candidate)

    # 3. Shuffle first to randomize ties, then stable-sort by length descending
    random.shuffle(results)
    results.sort(key=len, reverse=True)

    return results



def get_random_word(file_path="rndwords.txt"):
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

words = load_words('words.txt')
word = get_random_word('rndwords.txt')
anagrams = get_anagrams(word, words)
print(word)
print(anagrams)
