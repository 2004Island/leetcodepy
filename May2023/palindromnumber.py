# Fourth LC problem May 18th


class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

test = Solution()

# Input: x = 121
print(test.isPalindrome(x = 121))
# Returns True

# Input: x = -121
print(test.isPalindrome(x = -121))
# Returns False

# Input: x = 10
print(test.isPalindrome(x = 10))
# Returns False