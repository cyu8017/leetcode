// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

int maximumXorProduct(long long a, long long b, int n) {
    const int mod = 1000000007;
    for (int i = n - 1; i >= 0; i--) {
        long long bit = 1LL << i;
        long long abit = a & bit, bbit = b & bit;
        if (abit == bbit) { a |= bit; b |= bit; }
        else if (a > b) { b |= bit; a &= ~bit; }
        else { a |= bit; b &= ~bit; }
    }
    return (int)((a % mod) * (b % mod) % mod);
}
