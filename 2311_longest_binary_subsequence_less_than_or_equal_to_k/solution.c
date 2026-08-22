// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

#include <string.h>

int longestSubsequence(char* s, int k) {
    int zeros = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) if (s[i] == '0') zeros++;
    long long val = 0;
    int ones = 0;
    long long pow = 1;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '1') {
            if (pow > k || val + pow > k) {
                // skip
            } else {
                val += pow;
                ones++;
            }
        }
        if (pow <= k) pow <<= 1;
    }
    return zeros + ones;
}
