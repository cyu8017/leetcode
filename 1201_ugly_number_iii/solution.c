// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

static long long gcdll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static long long lcmll(long long a, long long b) {
    return a / gcdll(a, b) * b;
}

int nthUglyNumber(int n, int a, int b, int c) {
    long long ab = lcmll(a, b);
    long long ac = lcmll(a, c);
    long long bc = lcmll(b, c);
    long long abc = lcmll(ab, c);
    long long lo = 1, hi = 2000000000LL;
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        long long cnt = mid / a + mid / b + mid / c - mid / ab - mid / ac - mid / bc + mid / abc;
        if (cnt >= n) hi = mid;
        else lo = mid + 1;
    }
    return (int)lo;
}
