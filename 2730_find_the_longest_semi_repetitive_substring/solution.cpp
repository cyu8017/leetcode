// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

#include <string>
#include <algorithm>

class Solution {
public:
    int longestSemiRepetitiveSubstring(std::string s) {
        int ans = 0, left = 0, lastPair = -1;
        for (int right = 0; right < (int)s.size(); right++) {
            if (right > 0 && s[right] == s[right - 1]) {
                if (lastPair >= left) left = lastPair + 1;
                lastPair = right - 1;
            }
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
