// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

#include <string>

class Solution {
    int expand(const std::string& s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < static_cast<int>(s.size()) && s[left] == s[right]) {
            ++count;
            --left;
            ++right;
        }
        return count;
    }

public:
    int countSubstrings(std::string s) {
        int total = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            total += expand(s, i, i);
            total += expand(s, i, i + 1);
        }
        return total;
    }
};
