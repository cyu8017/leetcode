// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

#include <climits>
#include <cstdlib>

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        bool negative = (dividend < 0) ^ (divisor < 0);
        long long absDividend = llabs(static_cast<long long>(dividend));
        long long absDivisor = llabs(static_cast<long long>(divisor));

        int quotient = 0;
        for (int i = 31; i >= 0; i--) {
            if ((absDividend >> i) >= absDivisor) {
                quotient += 1 << i;
                absDividend -= absDivisor << i;
            }
        }

        return negative ? -quotient : quotient;
    }
};
