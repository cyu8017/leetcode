// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

#include <string>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        int bestStart = 0;
        int bestLen = 0;

        for (int i = 0; i < static_cast<int>(s.size()); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i + 1);
            int len = std::max(len1, len2);
            if (len > bestLen) {
                bestLen = len;
                bestStart = i - (len - 1) / 2;
            }
        }

        return s.substr(bestStart, bestLen);
    }

private:
    static int expand(const std::string& s, int left, int right) {
        while (left >= 0 && right < static_cast<int>(s.size()) && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
};
