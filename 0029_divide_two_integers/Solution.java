// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long absDividend = Math.abs((long) dividend);
        long absDivisor = Math.abs((long) divisor);

        int quotient = 0;
        for (int i = 31; i >= 0; i--) {
            if ((absDividend >> i) >= absDivisor) {
                quotient += 1 << i;
                absDividend -= absDivisor << i;
            }
        }

        return negative ? -quotient : quotient;
    }
}
