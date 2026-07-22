// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

#include <algorithm>
#include <string>

class Solution {
public:
    int minimumDeletions(std::string s) {
        int b = 0;
        int ans = 0;
        for (char c : s) {
            if (c == 'b') {
                ++b;
            } else {
                ans = std::min(ans + 1, b);
            }
        }
        return ans;
    }
};
