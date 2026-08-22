// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

static int modPow(long long a, int b) {
    const int mod = 1000000007;
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return (int)res;
}

int stringCount(int n) {
    const int mod = 1000000007;
    if (n < 4) return 0;
    long long ans = modPow(26, n);
    ans = (ans - 3LL * modPow(25, n) % mod + mod) % mod;
    ans = (ans + 3LL * modPow(24, n) % mod) % mod;
    ans = (ans - modPow(23, n) + mod) % mod;
    ans = (ans + 1LL * (n % mod) * modPow(25, n - 1) % mod) % mod;
    ans = (ans - 2LL * (n % mod) % mod * modPow(24, n - 1) % mod + mod) % mod;
    ans = (ans + 1LL * (n % mod) * modPow(23, n - 1) % mod) % mod;
    ans = (ans - 1LL * (n % mod) * ((n - 1 + mod) % mod) % mod * modPow(24, n - 2) % mod % mod + mod) % mod;
    ans = (ans + 1LL * (n % mod) * ((n - 1 + mod) % mod) % mod * modPow(23, n - 2) % mod) % mod;
    return (int)ans;
}
