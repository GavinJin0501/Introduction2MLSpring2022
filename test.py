def checkInclusion(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)

    if n1 > n2:
        return False

    for i in range(n2 - n1 + 1):
        temp = [0] * 26
        for j in range(i, i + n1):
            temp[ord(s2[i]) - ord('a')] += 1
        print(temp)
        for each in s1:
            temp[ord(each) - ord('a')] -= 1
        print(temp)
        status = True
        for each in temp:
            if each != 0:
                status = False
        if status:
            return status
        print()
    return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))

