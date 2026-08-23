// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

#include <string>

class Solution {
public:
    bool scoreBalance(std::string s) {
        int l = 0, r = 0;
        for (char c : s) r += (c - 'a') + 1;
        for (int i = 0; i + 1 < (int)s.size(); i++) {
            int x = (s[i] - 'a') + 1;
            l += x;
            r -= x;
            if (l == r) return true;
        }
        return false;
    }
};
