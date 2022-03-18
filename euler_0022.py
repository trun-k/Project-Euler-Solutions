"""
Problem 22: Names scores
------------------------


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

"""

def read_file():
    file = open('names.txt')
    names = []
    for i in file:
        names.append(i)
    return names


def get_names():
    names = read_file()[0].split(",")
    return sorted(names)


def score(name):
    name = name[1:len(name)-1]
    sum = 0
    for i in name:
        sum += (ord(i)-64)
    return sum


def solve(namelist):
    ans = 0
    i = 1
    for name in namelist:
        ans += (i*score(name))
        i += 1
    return ans


def compute():
    names = get_names()
    return solve(names)
    