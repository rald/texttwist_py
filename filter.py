import random

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

    return results

words=[]
with open('words.txt', 'r', encoding='utf-8') as f:
	for line in f:
		w = line.strip().lower()
		if w:
			words.append(w)


with open('rndwords.txt', 'w', encoding='utf-8') as f:
	for word in words:
		if len(word)!=6: continue
		anagrams=get_anagrams(word,words);
		if len(anagrams)>=10 and len(anagrams)<=48:
			f.write(word+'\n')
			print(word)

