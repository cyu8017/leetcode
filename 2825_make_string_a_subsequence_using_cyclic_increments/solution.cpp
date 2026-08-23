// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

#include <string>

class Solution {
public:
    bool canMakeSubsequence(std::string str1, std::string str2) {
        int j = 0;
        for (int i = 0; i < (int)str1.size() && j < (int)str2.size(); i++) {
            char a = str1[i], b = str2[j];
            if (a == b || (a - 'a' + 1) % 26 == (b - 'a')) j++;
        }
        return j == (int)str2.size();
    }
};
