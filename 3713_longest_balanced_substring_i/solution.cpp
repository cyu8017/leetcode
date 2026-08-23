// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

#include <algorithm>
#include <string>

class Solution {
public:
    int longestBalanced(std::string s) {
        int n = (int)s.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt[26] = {};
            int mx = 0, v = 0;
            for (int j = i; j < n; j++) {
                int c = s[j] - 'a';
                cnt[c]++;
                if (cnt[c] == 1) v++;
                mx = std::max(mx, cnt[c]);
                if (mx * v == j - i + 1) ans = std::max(ans, j - i + 1);
            }
        }
        return ans;
    }
};
