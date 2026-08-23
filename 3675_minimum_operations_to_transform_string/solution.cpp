// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minOperations(std::string s) {
        int ans = 0;
        for (char c : s) {
            if (c != 'a') ans = std::max(ans, 26 - (c - 'a'));
        }
        return ans;
    }
};
