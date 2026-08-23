// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

class Solution {
    public int maximumXorProduct(long a, long b, int n) {
        final int mod = 1000000007;
        for (int i = n - 1; i >= 0; i--) {
            long bit = 1L << i;
            long abit = a & bit, bbit = b & bit;
            if (abit == bbit) {
                a |= bit;
                b |= bit;
            } else if (a > b) {
                b |= bit;
                a &= ~bit;
            } else {
                a |= bit;
                b &= ~bit;
            }
        }
        return (int)((a % mod) * (b % mod) % mod);
    }
}
