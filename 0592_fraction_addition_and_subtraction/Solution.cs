// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

public class Solution {
    public string FractionAddition(string expression) {
        long numerator = 0, denominator = 1;
        int i = 0, len = expression.Length;
        while (i < len) {
            int sign = 1;
            if (expression[i] == '+' || expression[i] == '-') {
                if (expression[i] == '-') sign = -1;
                ++i;
            }
            long a = 0;
            while (i < len && expression[i] >= '0' && expression[i] <= '9') {
                a = a * 10 + (expression[i] - '0');
                ++i;
            }
            a *= sign;
            ++i; // skip '/'
            long b = 0;
            while (i < len && expression[i] >= '0' && expression[i] <= '9') {
                b = b * 10 + (expression[i] - '0');
                ++i;
            }
            numerator = numerator * b + a * denominator;
            denominator *= b;
            long g = Gcd(System.Math.Abs(numerator), System.Math.Abs(denominator));
            numerator /= g;
            denominator /= g;
        }
        return numerator + "/" + denominator;
    }

    private long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
