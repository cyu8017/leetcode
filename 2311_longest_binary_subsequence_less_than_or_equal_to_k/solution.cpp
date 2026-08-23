// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

#include <string>

class Solution {
public:
    int longestSubsequence(std::string s, int k) {
        int zeros = 0;
        for (char c : s) if (c == '0') zeros++;
        long long val = 0;
        int ones = 0;
        long long pow = 1;
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            if (s[i] == '1') {
                if (pow > k || val + pow > k) {
                    // skip
                } else {
                    val += pow;
                    ones++;
                }
            }
            if (pow <= k) {
                if (pow > (1LL << 60)) pow = k + 1;
                else pow <<= 1;
            }
        }
        return zeros + ones;
    }
};
