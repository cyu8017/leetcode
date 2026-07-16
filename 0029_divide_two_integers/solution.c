// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

#include <limits.h>
#include <stdlib.h>

int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }

    int negative = (dividend < 0) ^ (divisor < 0);
    long long absDividend = llabs((long long)dividend);
    long long absDivisor = llabs((long long)divisor);

    int quotient = 0;
    for (int i = 31; i >= 0; i--) {
        if ((absDividend >> i) >= absDivisor) {
            quotient += 1 << i;
            absDividend -= absDivisor << i;
        }
    }

    return negative ? -quotient : quotient;
}
