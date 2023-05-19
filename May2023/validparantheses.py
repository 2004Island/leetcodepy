# Fifth LC problem May 18th


class Solution:

    def isValid(self, s: str) -> bool:
        
        completeset = {}
        end = len(s) - 1
        i = 0

        while i < end:

            if s[i] + s[i + 1] not in completeset:
                return False
            
            i += 2

        return True


test = Solution()

# Input: s = "()"
print(test.isValid("()"))
# Output: true

# Input: s = "()[]{}"
print(test.isValid("()[]{}"))
# Output: true

# Input: s = "(]"
print(test.isValid("(]"))
# Output: false

# Input s = "{[]}"
print(test.isValid("{[]}"))
# Output: true