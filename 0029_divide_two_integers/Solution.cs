// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

public class Solution {
    public int Divide(int dividend, int divisor) {
        if (dividend == int.MinValue && divisor == -1) {
            return int.MaxValue;
        }

        bool negative = (dividend < 0) ^ (divisor < 0);
        long a = Math.Abs((long)dividend);
        long b = Math.Abs((long)divisor);
        long quotient = 0;

        for (int i = 31; i >= 0; i--) {
            if ((a >> i) >= b) {
                quotient += 1L << i;
                a -= b << i;
            }
        }

        return negative ? (int)-quotient : (int)quotient;
    }
}
