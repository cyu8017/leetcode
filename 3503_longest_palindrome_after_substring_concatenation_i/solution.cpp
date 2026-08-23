// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
    void expand(const std::string& s, std::vector<int>& g, int l, int r) {
        while (l >= 0 && r < (int)s.size() && s[l] == s[r]) {
            g[l] = std::max(g[l], r - l + 1);
            l--; r++;
        }
    }
    std::vector<int> calc(const std::string& s) {
        int n = (int)s.size();
        std::vector<int> g(n);
        for (int i = 0; i < n; i++) {
            expand(s, g, i, i);
            expand(s, g, i, i + 1);
        }
        return g;
    }
public:
    int longestPalindrome(std::string s, std::string t) {
        int m = (int)s.size(), n = (int)t.size();
        std::reverse(t.begin(), t.end());
        auto g1 = calc(s), g2 = calc(t);
        int ans = 0;
        for (int v : g1) ans = std::max(ans, v);
        for (int v : g2) ans = std::max(ans, v);
        std::vector<std::vector<int>> f(m + 1, std::vector<int>(n + 1));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    int a = (i < m) ? g1[i] : 0;
                    int b = (j < n) ? g2[j] : 0;
                    ans = std::max(ans, f[i][j] * 2 + a);
                    ans = std::max(ans, f[i][j] * 2 + b);
                }
            }
        }
        return ans;
    }
};
