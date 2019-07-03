"""
子符串匹配算法：
给定一个主字符串和模式串，在主串是否存在模式串

解决思路：
1. 暴力破解 bf
2. rk算法，主要是哈希函数的设计，这个地方我用到python内置的hash函数
3. bm算法，坏字符，好后缀
"""


def bf_match(pattern, string):
    found = None
    for i, s in enumerate(string):
        j = i
        for t in pattern:
            if j < len(string) and t == string[j]:
                j += 1
            else:
                break
        else:
            found = i
            break
    return found


def rk_match(pattern, string):
    found = None
    length = len(pattern)
    if length > len(string):
        return found
    left = 0
    right = length
    pattern_hash = hash(pattern)
    while right <= len(string):
        value = hash(string[left:right])
        if value == pattern_hash:
            found = left
            break
        left += 1
        right += 1
    return found


def bm_match(pattern, string):
    found = None
    left = 0
    right = len(pattern)-1
    while right < len(string):
        pos = len(pattern) - 1
        while pos >= 0:
            if pattern[pos] != string[right-(len(pattern)-1-pos)]:
                x = find_s(pattern, string[right-(len(pattern)-1-pos)])
                right = right + pos - x
                break
            pos -= 1
        else:
            found = right
            break
    if found:
        return found - len(pattern) + 1
    return found


def find_s(pattern, s):
    try:
        index = pattern.index(s)
        return index
    except:
        return -1



if __name__ == "__main__":
    # print(bf_match('abc', 'a'))
    # print(rk_match('abc', 'aaadabcbc'))
    print(bm_match('abc', 'aaadabcbc'))

