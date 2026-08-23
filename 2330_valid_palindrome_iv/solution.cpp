// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

#include <string>

class Solution {
public:
    bool makePalindrome(std::string s) {
        int diff = 0;
        for (int i = 0, j = (int)s.size() - 1; i < j; ++i, --j) {
            if (s[i] != s[j]) {
                diff++;
                if (diff > 2) return false;
            }
        }
        return true;
    }
};
