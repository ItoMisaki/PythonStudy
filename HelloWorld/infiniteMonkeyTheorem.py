import random


def genRandomStr(length):
    rs_str = ""

    ch_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
               5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
               10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
               15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
               20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
               25: 'z', 26: ' '}

    for i in range(length):
        random.seed()
        k = random.randint(0, 26)
        rs_str += ch_dict[k]

    return rs_str


def scoreRandomStr(base_str, random_str):
    score = 0

    if len(base_str) != len(random_str):
        return  score
    else:
        for i in range(len(base_str)):
            if base_str[i] == random_str[i]:
                score += 1
            else:
                continue
        return score


def callInfiniteMonkeyTheorem(base_str, count):
    while(True):

        best_str = ""
        best_score = 0

        for i in range(count):

            random_str = genRandomStr(len(base_str))

            if scoreRandomStr(base_str, random_str) == len(base_str):
                best_score = len(base_str)
                best_str = random_str
                print("{0}:{1}".format(best_score, best_str))
                return best_str
            else:
                score = scoreRandomStr(base_str, random_str)
                if score > best_score:
                    best_score = score
                    best_str = random_str

        print("{0}:{1}".format(best_score, best_str))


def main():
    base_str = "love"

    callInfiniteMonkeyTheorem(base_str, 1000)

main()