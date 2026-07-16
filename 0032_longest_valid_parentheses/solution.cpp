// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

#include <algorithm>
#include <stack>
#include <string>

class Solution {
public:
    int longestValidParentheses(std::string s) {
        std::stack<int> stack;
        stack.push(-1);
        int best = 0;

        for (int i = 0; i < static_cast<int>(s.size()); i++) {
            if (s[i] == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    best = std::max(best, i - stack.top());
                }
            }
        }

        return best;
    }
};
