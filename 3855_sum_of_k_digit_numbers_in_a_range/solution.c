// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

static long long qpow3855(long long a, long long n, long long mod) {
    a %= mod;
    long long ans = 1;
    while (n > 0) {
        if (n & 1) ans = ans * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return ans;
}

int sumOfNumbers(int l, int r, int k) {
    const long long mod = 1000000007;
    long long n = (long long)r - l + 1;
    long long sum = (long long)(l + r) * n / 2 % mod;
    long long part1 = qpow3855(n % mod, k - 1, mod);
    long long part2 = (qpow3855(10, k, mod) - 1 + mod) % mod;
    long long inv9 = qpow3855(9, mod - 2, mod);
    long long ans = sum;
    ans = ans * part1 % mod;
    ans = ans * part2 % mod;
    ans = ans * inv9 % mod;
    return (int)ans;
}
