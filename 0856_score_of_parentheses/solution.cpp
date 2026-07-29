// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int scoreOfParentheses(std::string s) {
        std::vector<int> stack{0};
        for (char ch : s) {
            if (ch == '(') {
                stack.push_back(0);
            } else {
                int val = stack.back();
                stack.pop_back();
                stack.back() += std::max(2 * val, 1);
            }
        }
        return stack[0];
    }
};
