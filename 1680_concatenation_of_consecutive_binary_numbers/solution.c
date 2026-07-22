// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

int concatenatedBinary(int n) {
    long long ans = 0;
    int bits = 0;
    const int mod = 1000000007;
    for (int x = 1; x <= n; x++) {
        if ((x & (x - 1)) == 0) bits++;
        ans = ((ans << bits) + x) % mod;
    }
    return (int)ans;
}
