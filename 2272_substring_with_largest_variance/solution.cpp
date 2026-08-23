// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

#include <string>
#include <algorithm>

class Solution {
public:
    int largestVariance(std::string s) {
        int ans = 0;
        for (char a = 'a'; a <= 'z'; ++a) {
            for (char b = 'a'; b <= 'z'; ++b) {
                if (a == b) continue;
                int bal = 0;
                bool hasB = false;
                for (char c : s) {
                    if (c == a) bal++;
                    else if (c == b) { bal--; hasB = true; }
                    if (hasB) ans = std::max(ans, bal);
                    if (bal < 0) { bal = 0; hasB = false; }
                }
            }
        }
        return ans;
    }
};
