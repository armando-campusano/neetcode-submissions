from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    some_dict = {}
    for char in word:
        if char in some_dict:
            some_dict[char] += 1
        else:
            some_dict[char] = 1
    return some_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
