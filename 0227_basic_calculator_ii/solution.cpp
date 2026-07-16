// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

#include <cctype>
#include <stack>
#include <string>

class Solution {
public:
    int calculate(std::string s) {
        std::stack<int> values;
        int number = 0;
        char operatorChar = '+';

        for (int index = 0; index < static_cast<int>(s.size()); index++) {
            char ch = s[index];
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                number = number * 10 + (ch - '0');
            }
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == static_cast<int>(s.size()) - 1) {
                if (operatorChar == '+') {
                    values.push(number);
                } else if (operatorChar == '-') {
                    values.push(-number);
                } else if (operatorChar == '*') {
                    int prev = values.top();
                    values.pop();
                    values.push(prev * number);
                } else if (operatorChar == '/') {
                    int prev = values.top();
                    values.pop();
                    values.push(prev / number);
                }
                operatorChar = ch;
                number = 0;
            }
        }

        int total = 0;
        while (!values.empty()) {
            total += values.top();
            values.pop();
        }
        return total;
    }
};
