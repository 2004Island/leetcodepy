# Second LC problem May 18th
# Apparently this answer is extremely inefficient so I may rework it in future


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        listofsplitwords = [[*x] for x in strs]
        returnstr = ""
        condition = True
        testvar = True
        
        while condition:

            for i in range(len(listofsplitwords[0])): 
                for j in listofsplitwords: # iterates through each word in list of words
                    if i >= len(j): # if iterator is greater than any other word len that means the current returnstr is the lcp 
                        return returnstr
                    else:
                        if listofsplitwords[0][i] == j[i]: # if the nth letter of the first word is the same as the nth letter of the jth word that makes it common
                            continue
                        else:
                            testvar = False
                if testvar:
                    returnstr += listofsplitwords[0][i]
            
            return returnstr

test = Solution()

# Input: strs = ["flower","flow","flight"]
strs = ["flower","flow","flight"]
print(test.longestCommonPrefix(strs))
# Returns "fl"

# Input: strs = ["dog","racecar","car"]
strs = ["dog","racecar","car"]
print(test.longestCommonPrefix(strs))
# Returns ""