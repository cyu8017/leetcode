// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

static int digitSum2457(long long x) {
    int s = 0;
    while (x > 0) {
        s += (int)(x % 10);
        x /= 10;
    }
    return s;
}

long long makeIntegerBeautiful(long long n, int target) {
    long long orig = n;
    long long pow = 1;
    while (digitSum2457(n) > target) {
        n = n / 10 + 1;
        pow *= 10;
    }
    return n * pow - orig;
}
