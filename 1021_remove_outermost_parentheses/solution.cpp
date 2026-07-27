// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

#include <string>

class Solution {
public:
    std::string removeOuterParentheses(std::string s) {
        std::string ans;
        int depth = 0;
        for (char ch : s) {
            if (ch == '(') {
                if (depth) ans.push_back(ch);
                ++depth;
            } else {
                --depth;
                if (depth) ans.push_back(ch);
            }
        }
        return ans;
    }
};

