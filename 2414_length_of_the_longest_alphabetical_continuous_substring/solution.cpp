// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

#include <algorithm>
#include <string>

class Solution {
public:
    int longestContinuousSubstring(std::string s) {
        int ans = 1, cur = 1;
        for (int i = 1; i < (int)s.size(); i++) {
            if (s[i] == s[i - 1] + 1) {
                cur++;
                ans = std::max(ans, cur);
            } else {
                cur = 1;
            }
        }
        return ans;
    }
};
