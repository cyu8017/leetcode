// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

#include <string>
#include <vector>

class Solution {
public:
    bool parseBoolExpr(std::string expression) {
        std::vector<char> stack;
        for (char ch : expression) {
            if (ch == ')') {
                std::vector<bool> values;
                while (!stack.empty() && stack.back() != '&' && stack.back() != '|' &&
                       stack.back() != '!') {
                    char token = stack.back();
                    stack.pop_back();
                    if (token == 't' || token == 'f') {
                        values.push_back(token == 't');
                    }
                }
                char op = stack.back();
                stack.pop_back();
                if (op == '!') {
                    stack.push_back(values[0] ? 'f' : 't');
                } else if (op == '&') {
                    bool all = true;
                    for (bool v : values) {
                        all = all && v;
                    }
                    stack.push_back(all ? 't' : 'f');
                } else {
                    bool any = false;
                    for (bool v : values) {
                        any = any || v;
                    }
                    stack.push_back(any ? 't' : 'f');
                }
            } else if (ch != ',') {
                stack.push_back(ch);
            }
        }
        return stack.back() == 't';
    }
};
