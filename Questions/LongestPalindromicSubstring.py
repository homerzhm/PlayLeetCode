"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

"""

import math


def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

class Solution(object):
    def longestPalindrome(self, s):

        return self.solution1(s)



    def solution1(self, s):
        theMaxLenght = 0
        result = ''
        length = len(s)
        i = 0
        cache = {}
        maxLengthOfPString = math.floor(len(s) / 2)
        print maxLengthOfPString
        while i < length:
            character = s[i]
            j = 0
            while j <= maxLengthOfPString:
                print i , i + j
                if i + j >= length:
                    break;
                cacheKey = s[i:i+j]
                cache[cacheKey] = i
                print reverse(cacheKey), cacheKey, cache
                if cache.has_key(reverse(cacheKey)):
                    if len(cacheKey) * 2 > theMaxLenght or len(cacheKey) * 2 + 1 > theMaxLenght:
                        if (cache[reverse(cacheKey)] + len(cacheKey)) == cache[cacheKey]:
                            theMaxLenght = len(cacheKey) * 2
                            result = reverse(cacheKey) + cacheKey

                        elif cache[cacheKey] + len(cacheKey) == cache[reverse(cacheKey)]:
                            theMaxLenght = len(cacheKey) * 2
                            result = cacheKey + reverse(cacheKey)

                        elif cache[reverse(cacheKey)] + len(cacheKey)+ 1 == cache[cacheKey]:
                            theMaxLenght = len(cacheKey) * 2 + 1
                            result = reverse(cacheKey) + s[cache[reverse(cacheKey)] + len(cacheKey) + 1] + cacheKey

                        elif cache[cacheKey] + len(cacheKey)+ 1 == cache[reverse(cacheKey)]:
                            theMaxLenght = len(cacheKey) * 2 + 1
                            result = cacheKey + s[cache[cacheKey] + len(cacheKey)+ 1] + reverse(cacheKey)
                j += 1
            i += 1
        print cache
        return result

def main():
    testCase = "babad"
    s = Solution()
    print s.longestPalindrome(testCase)

if __name__ == '__main__':
    main()