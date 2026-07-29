// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    int calculate(std::string s) {
        std::string expr;
        for (char ch : s) {
            if (!std::isspace(static_cast<unsigned char>(ch))) {
                expr.push_back(ch);
            }
        }
        int i = 0;
        return parse(expr, i);
    }

private:
    int parse(const std::string& expr, int& i) {
        std::vector<long long> stack;
        long long num = 0;
        char sign = '+';
        while (i < static_cast<int>(expr.size())) {
            char ch = expr[i];
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                num = num * 10 + (ch - '0');
            } else if (ch == '(') {
                ++i;
                num = parse(expr, i);
            }
            if ((!std::isdigit(static_cast<unsigned char>(ch)) && ch != '(') ||
                i == static_cast<int>(expr.size()) - 1) {
                if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' ||
                    i == static_cast<int>(expr.size()) - 1) {
                    if (sign == '+') {
                        stack.push_back(num);
                    } else if (sign == '-') {
                        stack.push_back(-num);
                    } else if (sign == '*') {
                        stack.back() *= num;
                    } else if (sign == '/') {
                        long long top = stack.back();
                        stack.pop_back();
                        stack.push_back(static_cast<long long>(top / static_cast<double>(num)));
                    }
                    if (ch == ')') {
                        long long sum = 0;
                        for (long long v : stack) {
                            sum += v;
                        }
                        return static_cast<int>(sum);
                    }
                    sign = ch;
                    num = 0;
                }
            }
            ++i;
        }
        long long sum = 0;
        for (long long v : stack) {
            sum += v;
        }
        return static_cast<int>(sum);
    }
};
