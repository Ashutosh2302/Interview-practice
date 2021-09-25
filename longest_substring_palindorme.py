def longestsubstringpalindrome(s):
    palindromes = {}
    for i in range(len(s)):
        string = ''
        for j in range(i, len(s)):
            string += s[j]
            if string == string[::-1]:
                palindromes[string] = len(string)

    max_len = max(palindromes.values())
    for key, value in palindromes.items():
        if value == max_len:
            return key


print(longestsubstringpalindrome('abaxyzzyxf'))
