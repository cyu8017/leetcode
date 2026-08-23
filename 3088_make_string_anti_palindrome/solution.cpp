// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string makeAntiPalindrome(std::string s) {
        std::sort(s.begin(), s.end());
        int n = (int)s.size();
        int m = n / 2;
        if (s[m] == s[m - 1]) {
            int i = m;
            while (i < n && s[i] == s[i - 1]) i++;
            for (int j = m; j < n && s[j] == s[n - j - 1]; i++, j++) {
                if (i >= n) return "-1";
                std::swap(s[i], s[j]);
            }
        }
        return s;
    }
};
