def exractNum(s):
    l = []
    for t in s1.split():
        try:
            l.append(float(t))
        except ValueError:
            pass

    return l


def compare(s1, s2):
    l1 = exractNum(s1)
    l2 = exractNum(s2)
    if len(l1) == 0 or len(l2) == 0:
        # string contain no numbers
        compareAlpha(s1, s2)
    else:
        compareNum(l1, l2)


def compareNum(l1, l2):
    for i in range(0, (min(len(l1), len(l2)))):
        if l1[i] > l2[i]:
            print(s1 + " > " + s2)
            break
        elif l1[i] < l2[i]:
            print(s1 + " < " + s2)
            break


def compareAlpha(s1, s2):
    if s1.lower() == s1.lower():
        print(s1 + " = " + s2)
    elif s1.lower() > s2.lower():
        print(s1 + " > " + s2)
    elif s1.lower() < s2.lower():
        print(s1 + " < " + s2)
    else:
        compareLength(s1, s2)


def compareLength(s1, s2):
    if len(s1) > len(s2):
        print(s1 + " > " + s2)
    elif len(s1) < len(s2):
        print(s1 + " < " + s2)
    else:
        print("No comparison possible")


s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if s1 == s2:
    print(s1 + " = " + s2)
else:
    compare(s1, s2)

# Test cases:
# 1.2:3.4
# 1.2gb:3.4gb
#  :
# aa:aaa
# aaa:aaa
# abv:des
# Aa:aa

# Note: After writing this I realise the question could also be answered with method overloading
