// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

#include <cctype>
#include <string>
#include <utility>

class Solution {
    std::pair<int, int> parse(const std::string& expr) {
        int coef = 0;
        int constant = 0;
        const int n = static_cast<int>(expr.size());
        int i = 0;
        while (i < n) {
            int sign = 1;
            if (expr[i] == '+' || expr[i] == '-') {
                sign = expr[i] == '-' ? -1 : 1;
                ++i;
            }
            int value = 0;
            bool hasDigit = false;
            while (i < n && std::isdigit(static_cast<unsigned char>(expr[i]))) {
                hasDigit = true;
                value = value * 10 + (expr[i] - '0');
                ++i;
            }
            if (i < n && expr[i] == 'x') {
                coef += sign * (hasDigit ? value : 1);
                ++i;
            } else {
                constant += sign * value;
            }
        }
        return {coef, constant};
    }

public:
    std::string solveEquation(std::string equation) {
        const auto eq = equation.find('=');
        auto [leftCoef, leftConst] = parse(equation.substr(0, eq));
        auto [rightCoef, rightConst] = parse(equation.substr(eq + 1));
        const int coef = leftCoef - rightCoef;
        const int constant = rightConst - leftConst;
        if (coef == 0) {
            return constant == 0 ? "Infinite solutions" : "No solution";
        }
        return "x=" + std::to_string(constant / coef);
    }
};
