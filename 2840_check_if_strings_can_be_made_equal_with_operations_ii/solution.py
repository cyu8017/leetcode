# LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0] * 26
        odd1 = [0] * 26
        even2 = [0] * 26
        odd2 = [0] * 26
        for i in range(len(s1)):
            if i % 2 == 0:
                even1[ord(s1[i]) - 97] += 1
                even2[ord(s2[i]) - 97] += 1
            else:
                odd1[ord(s1[i]) - 97] += 1
                odd2[ord(s2[i]) - 97] += 1
        return even1 == even2 and odd1 == odd2
