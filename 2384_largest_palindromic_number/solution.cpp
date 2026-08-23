// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

#include <string>

class Solution {
public:
    std::string largestPalindromic(std::string num) {
        int cnt[10] = {};
        for (char c : num) cnt[c - '0']++;
        std::string left;
        for (int d = 9; d >= 0; d--) {
            while (cnt[d] >= 2) {
                if (d == 0 && left.empty()) break;
                left.push_back(char('0' + d));
                cnt[d] -= 2;
            }
        }
        char mid = 0;
        for (int d = 9; d >= 0; d--) {
            if (cnt[d] > 0) {
                mid = char('0' + d);
                break;
            }
        }
        if (left.empty()) {
            if (mid) return std::string(1, mid);
            return "0";
        }
        std::string right(left.rbegin(), left.rend());
        if (mid) return left + mid + right;
        return left + right;
    }
};
