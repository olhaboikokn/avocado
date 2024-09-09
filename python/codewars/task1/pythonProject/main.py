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

#You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity
# to go for a short walk. The city provides its citizens with a
# Walk Generating App on their phones -- everytime you press the button
# it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you know it takes you one minute
# to traverse one city block, so create a function that will return true if the walk the app gives you will
# take you exactly ten minutes (you don't want to be early or late!) and will, of course,
# return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) != 10:
        return False
    x, y = 0, 0
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    return x == 0 and y == 0


if __name__ == "__main__":
    test_walk_1 = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
    test_walk_2 = ['n', 'n', 'e', 'e', 's', 's', 'w', 'w', 'n']
    result = is_valid_walk(walk=test_walk_2)
    print(result)

