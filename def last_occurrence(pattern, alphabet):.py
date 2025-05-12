def last_occurrence(pattern, alphabet):
    # Initialize all to -1
    L = {char: -1 for char in alphabet}
    for i, c in enumerate(pattern):
        L[c] = i  # Last occurrence of character c in pattern
    return L

def print_alignment(text, pattern, i, m):
    alignment = ' ' * (i - m + 1) + pattern
    print(text)
    print(alignment)
    print('-' * len(text))

def boyer_moore_match(text, pattern, alphabet):
    n = len(text)
    m = len(pattern)
    L = last_occurrence(pattern, alphabet)

    i = m - 1
    j = m - 1

    while i < n:
        print_alignment(text, pattern, i, m)

        if text[i] == pattern[j]:
            if j == 0:
                print_alignment(text, pattern, i, m)
                return i  # Match found
            else:
                i -= 1
                j -= 1
        else:
            l = L.get(text[i], -1)
            shift = m - min(j, 1 + l)
            i += shift
            j = m - 1  # Reset pattern index
    return -1  # No match found

# Example usage:
text = "algorithmicsalgorithms_align_almost_always"
pattern = "ways"
alphabet = set(text)

match_index = boyer_moore_match(text, pattern, alphabet)
print("Match found at index:", match_index if match_index != -1 else "Not found")
