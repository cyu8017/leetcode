// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

#include <string>

class Solution {
public:
    std::string parseTernary(std::string expression) {
        if (expression.find('?') == std::string::npos) {
            return expression;
        }

        int separator = 2;
        int depth = 0;
        for (int index = 2; index < static_cast<int>(expression.size()); ++index) {
            if (expression[index] == '?') {
                ++depth;
            } else if (expression[index] == ':') {
                if (depth == 0) {
                    separator = index;
                    break;
                }
                --depth;
            }
        }

        if (expression[0] == 'T') {
            return parseTernary(expression.substr(2, separator - 2));
        }
        return parseTernary(expression.substr(separator + 1));
    }
};
