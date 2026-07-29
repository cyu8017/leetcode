// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

#include <string>
#include <vector>

class Solution {
public:
    std::string reverseParentheses(std::string s) {
        std::vector<char> stack;
        for (char ch : s) {
            if (ch == ')') {
                std::string chunk;
                while (!stack.empty() && stack.back() != '(') {
                    chunk.push_back(stack.back());
                    stack.pop_back();
                }
                stack.pop_back();
                for (char c : chunk) stack.push_back(c);
            } else {
                stack.push_back(ch);
            }
        }
        return std::string(stack.begin(), stack.end());
    }
};
