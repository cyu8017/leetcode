// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

#include <string>
#include <vector>
#include <cctype>

class Solution {
public:
    std::vector<int> diffWaysToCompute(std::string expression) {
        std::vector<int> result;
        if (std::all_of(expression.begin(), expression.end(), [](unsigned char ch) { return std::isdigit(ch); })) {
            result.push_back(std::stoi(expression));
            return result;
        }
        for (int index = 0; index < static_cast<int>(expression.size()); ++index) {
            char operatorChar = expression[index];
            if (operatorChar != '+' && operatorChar != '-' && operatorChar != '*') {
                continue;
            }
            std::vector<int> left = diffWaysToCompute(expression.substr(0, index));
            std::vector<int> right = diffWaysToCompute(expression.substr(index + 1));
            for (int leftValue : left) {
                for (int rightValue : right) {
                    if (operatorChar == '+') {
                        result.push_back(leftValue + rightValue);
                    } else if (operatorChar == '-') {
                        result.push_back(leftValue - rightValue);
                    } else {
                        result.push_back(leftValue * rightValue);
                    }
                }
            }
        }
        return result;
    }
};
