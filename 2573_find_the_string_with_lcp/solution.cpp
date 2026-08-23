// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

#include <string>
#include <vector>

class Solution {
public:
    std::string findTheString(std::vector<std::vector<int>>& lcp) {
        int n = (int)lcp.size();
        std::string s(n, 0);
        char c = 'a';
        for (int i = 0; i < n; ++i) {
            if (s[i] != 0) continue;
            if (c > 'z') return "";
            s[i] = c;
            for (int j = i + 1; j < n; ++j) {
                if (lcp[i][j] > 0) s[j] = c;
            }
            c++;
        }
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int v = 0;
                if (s[i] == s[j]) {
                    v = 1;
                    if (i + 1 < n && j + 1 < n) v += lcp[i + 1][j + 1];
                }
                if (lcp[i][j] != v) return "";
            }
        }
        return s;
    }
};
