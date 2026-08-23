// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

#include <string>

class Solution {
public:
    int maximumLength(std::string s) {
        int n = (int)s.size(), ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (s[j] != s[i]) break;
                std::string sub = s.substr(i, j - i + 1);
                int cnt = 0, len = (int)sub.size();
                for (int k = 0; k + len <= n; k++) {
                    if (s.compare(k, len, sub) == 0) cnt++;
                }
                if (cnt >= 3 && len > ans) ans = len;
            }
        }
        return ans;
    }
};
