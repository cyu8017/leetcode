// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

#include <string>

class Solution {
public:
    bool backspaceCompare(std::string s, std::string t) {
        auto build = [](const std::string& text) {
            std::string stack;
            for (char ch : text) {
                if (ch == '#') {
                    if (!stack.empty()) {
                        stack.pop_back();
                    }
                } else {
                    stack.push_back(ch);
                }
            }
            return stack;
        };
        return build(s) == build(t);
    }
};
