// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

#include <string>
#include <algorithm>

class Solution {
public:
    std::string makeSmallestPalindrome(std::string s) {
        int n = (int)s.size();
        for (int i = 0; i < n / 2; i++) {
            char c = std::min(s[i], s[n - 1 - i]);
            s[i] = s[n - 1 - i] = c;
        }
        return s;
    }
};
