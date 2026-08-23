// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

#include <algorithm>
#include <string>

class Solution {
public:
    int almostPalindromic(std::string s) {
        int n = (int)s.size();
        auto f = [&](int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) {
                l--;
                r++;
            }
            int l1 = l - 1, r1 = r, l2 = l, r2 = r + 1;
            while (l1 >= 0 && r1 < n && s[l1] == s[r1]) {
                l1--;
                r1++;
            }
            while (l2 >= 0 && r2 < n && s[l2] == s[r2]) {
                l2--;
                r2++;
            }
            return std::min(n, std::max(r1 - l1 - 1, r2 - l2 - 1));
        };
        int ans = 0;
        for (int i = 0; i < n; i++) ans = std::max({ans, f(i, i), f(i, i + 1)});
        return ans;
    }
};
