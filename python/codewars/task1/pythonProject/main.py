"""A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""


def is_pangram(st):
    st = st.lower()
    letters = set()
    for char in st:
        if char.isalpha():
            letters.add(char)
    return len(letters) == 26


if __name__ == "__main__":
    test_string = "abcdf"
    result = is_pangram(st=test_string)
    print(result)
