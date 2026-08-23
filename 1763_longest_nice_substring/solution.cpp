// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

#include <cctype>
#include <string>

class Solution {
public:
    std::string longestNiceSubstring(std::string s) {
        int bestStart = 0;
        int bestLen = 0;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            int lower = 0;
            int upper = 0;
            for (int j = i; j < n; j++) {
                char c = s[j];
                if (std::islower((unsigned char)c)) {
                    lower |= 1 << (c - 'a');
                } else {
                    upper |= 1 << (c - 'A');
                }
                if (lower == upper && j - i + 1 > bestLen) {
                    bestStart = i;
                    bestLen = j - i + 1;
                }
            }
        }
        return s.substr(bestStart, bestLen);
    }
};
