// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

#include <string>

class Solution {
public:
    bool isFascinating(int n) {
        std::string s = std::to_string(n) + std::to_string(2 * n) + std::to_string(3 * n);
        if ((int)s.size() != 9) return false;
        int cnt[10] = {};
        for (char c : s) cnt[c - '0']++;
        if (cnt[0]) return false;
        for (int i = 1; i <= 9; i++) if (cnt[i] != 1) return false;
        return true;
    }
};
