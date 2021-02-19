def solution(s):
    answer = 0
    def expand(left, right, s):
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1, s), expand(i, i+2, s), key = len)

    answer = (len(result))
    return answer
