// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

#include <string>

class Solution {
    static void parse(const std::string& num, int& real, int& imag) {
        const size_t plus = num.find('+');
        real = std::stoi(num.substr(0, plus));
        imag = std::stoi(num.substr(plus + 1, num.size() - plus - 2));
    }

public:
    std::string complexNumberMultiply(std::string num1, std::string num2) {
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        parse(num1, a, b);
        parse(num2, c, d);

        const int real = a * c - b * d;
        const int imag = a * d + b * c;
        return std::to_string(real) + "+" + std::to_string(imag) + "i";
    }
};
