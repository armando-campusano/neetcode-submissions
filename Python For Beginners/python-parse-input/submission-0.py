from typing import List

def read_integers() -> List[int]:
    paragraph = input()
    listed_paragraph = paragraph.split(",")
    some_list = []

    for item in listed_paragraph:
        some_list.append(int(item))
        
    return some_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
