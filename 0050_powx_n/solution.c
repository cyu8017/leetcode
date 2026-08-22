// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

double myPow(double x, int n) {
    long exp = n;
    if (exp == 0) {
        return 1.0;
    }

    if (exp < 0) {
        x = 1.0 / x;
        exp = -exp;
    }

    double result = 1.0;
    double current = x;

    while (exp) {
        if (exp & 1) {
            result *= current;
        }
        current *= current;
        exp >>= 1;
    }

    return result;
}
