// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution {
    public String fractionAddition(String expression) {
        long numerator = 0;
        long denominator = 1;
        int i = 0;
        int len = expression.length();

        while (i < len) {
            int sign = 1;
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-') {
                if (expression.charAt(i) == '-') {
                    sign = -1;
                }
                ++i;
            }
            long a = 0;
            while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
                a = a * 10 + (expression.charAt(i) - '0');
                ++i;
            }
            a *= sign;
            ++i; // skip '/'
            long b = 0;
            while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
                b = b * 10 + (expression.charAt(i) - '0');
                ++i;
            }

            numerator = numerator * b + a * denominator;
            denominator *= b;
            long g = gcd(Math.abs(numerator), Math.abs(denominator));
            numerator /= g;
            denominator /= g;
        }

        return numerator + "/" + denominator;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
