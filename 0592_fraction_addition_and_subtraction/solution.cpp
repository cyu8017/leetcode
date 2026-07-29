// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

#include <cstdlib>
#include <numeric>
#include <string>

class Solution {
public:
    std::string fractionAddition(std::string expression) {
        long long numerator = 0;
        long long denominator = 1;
        int i = 0;
        int len = static_cast<int>(expression.size());

        while (i < len) {
            int sign = 1;
            if (expression[i] == '+' || expression[i] == '-') {
                if (expression[i] == '-') {
                    sign = -1;
                }
                ++i;
            }
            long long a = 0;
            while (i < len && expression[i] >= '0' && expression[i] <= '9') {
                a = a * 10 + (expression[i] - '0');
                ++i;
            }
            a *= sign;
            ++i;  // skip '/'
            long long b = 0;
            while (i < len && expression[i] >= '0' && expression[i] <= '9') {
                b = b * 10 + (expression[i] - '0');
                ++i;
            }

            numerator = numerator * b + a * denominator;
            denominator *= b;
            long long g = std::gcd(std::llabs(numerator), std::llabs(denominator));
            numerator /= g;
            denominator /= g;
        }

        return std::to_string(numerator) + "/" + std::to_string(denominator);
    }
};
