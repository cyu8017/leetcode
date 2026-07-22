// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

#include <algorithm>
#include <string>

class Solution {
public:
    int maxDepth(std::string s) {
        int depth = 0, ans = 0;
        for (char ch : s) {
            if (ch == '(') {
                ++depth;
                ans = std::max(ans, depth);
            } else if (ch == ')') {
                --depth;
            }
        }
        return ans;
    }
};
