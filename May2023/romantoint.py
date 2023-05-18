# First LC problem May 18th


class Solution(object):

    def romanToInt(self, s: str) -> int:

        sum = 0
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        splitlis = [*s]
        for i in range(len(splitlis)):

            if i < len(splitlis) - 1:
                if values[splitlis[i]] < values[splitlis[i+1]]:
                    sum -= values[splitlis[i]]
                else:
                    sum += values[splitlis[i]]
            else:
                sum += values[splitlis[i]]

        return sum

test = Solution()

# Input: s = "III"
print(test.romanToInt('III'))
# Returns 3

# Input: s = "LVIII"
print(test.romanToInt('LVIII'))
# Returns 58

# Input: s = "MCMXCIV"
print(test.romanToInt('MCMXCIV'))
# Returns 1994