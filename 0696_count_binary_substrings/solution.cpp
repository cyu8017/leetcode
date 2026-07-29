// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

#include <algorithm>
#include <string>

class Solution {
public:
    int countBinarySubstrings(std::string s) {
        int prev = 0;
        int cur = 1;
        int ans = 0;
        for (int i = 1; i < static_cast<int>(s.size()); ++i) {
            if (s[i] == s[i - 1]) {
                ++cur;
            } else {
                ans += std::min(prev, cur);
                prev = cur;
                cur = 1;
            }
        }
        return ans + std::min(prev, cur);
    }
};
