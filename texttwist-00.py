import random

PROMPT='> '

# --- Global Cache for words.txt to avoid redundant disk reads ---
_WORD_CACHE = None

def _load_dictionary(filename='words.txt'):
    global _WORD_CACHE
    if _WORD_CACHE is not None:
        return _WORD_CACHE
        
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                w = line.strip().lower()
                if w:
                    words.append(w)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
    _WORD_CACHE = words
    return _WORD_CACHE

def get_random_word(min_len=6, max_len=8, filename='words.txt'):
    """Picks a random word of length between min_len and max_len using cache."""
    words = _load_dictionary(filename)
    if not words:
        return None
        
    # Filter candidates by length
    valid_candidates = [w for w in words if min_len <= len(w) <= max_len]
    if not valid_candidates:
        return None
        
    return random.choice(valid_candidates)

def shuffle_word(word):
    """
    Shuffles a word using the optimal Fisher-Yates algorithm.
    Guarantees a distinct output for words with length > 1 without recursion.
    """
    n = len(word)
    if n <= 1:
        return word

    word_list = list(word)
    
    # Check if string consists of all identical characters (e.g., "aaaa")
    if len(set(word_list)) == 1:
        return word

    shuffled = word
    while shuffled == word:
        # Fisher-Yates Shuffle O(n)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            word_list[i], word_list[j] = word_list[j], word_list[i]
            
        shuffled = "".join(word_list)
        
    return shuffled
    
def get_anagrams(word, filename='words.txt'):
    """
    Finds all words (3+ letters) from the cached dictionary that can be formed 
    using the target word, sorted by length descending with random ties.
    """
    words = _load_dictionary(filename)
    if not words:
        return []
        
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

def index_of(matches, guess):
    """
    Returns the index of guess in matches, or -1 if not found.
    (Mimics JavaScript's Array.prototype.indexOf)
    """
    try:
        return matches.index(guess)
    except ValueError:
        return -1

def start_game:

    score = 0

    chosen_word = get_random_word()
    if not chosen_word: return

    matches = get_anagrams(chosen_word)
    num_matches = len(matches)
    guessed = [False] * num_matches

    scrambled = shuffle_word(chosen_word)
    print(f"TEXTTWIST {scrambled}")

    while running:
        guess = input(PROMPT)
        index = index_of(matches, guess)
        if index == -1: continue
        if guessed[index]:
            print(f"The word '{matches[index]}' is already guessed.")
            continue
        guessed[index] = True
        points = len(matches[index])
        score += points
        num_matches -= 1
        print(f"Plus {points} points. Score is now {score}.")
        if num_matches == 0:
            print(f"Game Complete!")            
            break

    print("Game Over.")
    print(f"Score is {score}")

if __name__ == "__main__":
    start_game()
