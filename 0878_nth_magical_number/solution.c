// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

#define MOD 1000000007

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int nthMagicalNumber(int n, int a, int b) {
    long long lcm = (long long)a / gcd(a, b) * b;
    long long lo = 1, hi = (long long)n * (a < b ? a : b);
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (mid / a + mid / b - mid / lcm >= n) hi = mid;
        else lo = mid + 1;
    }
    return (int)(lo % MOD);
}
