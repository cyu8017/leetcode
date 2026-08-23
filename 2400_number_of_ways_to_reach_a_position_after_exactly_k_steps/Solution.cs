// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

using System;

public class Solution {
    public int NumberOfWays(int startPos, int endPos, int k) {
        const int mod = 1000000007;
        int diff = Math.Abs(endPos - startPos);
        if (diff > k || (k - diff) % 2 != 0) return 0;
        int r = (k + diff) / 2;
        return Comb(k, r, mod);
    }

    private int Comb(int n, int r, int mod) {
        if (r < 0 || r > n) return 0;
        long num = 1, den = 1;
        for (int i = 0; i < r; i++) {
            num = num * (n - i) % mod;
            den = den * (i + 1) % mod;
        }
        return (int)(num * ModInverse((int)den, mod) % mod);
    }

    private int ModInverse(int a, int mod) => ModPow(a, mod - 2, mod);

    private int ModPow(int a, int e, int mod) {
        long res = 1, bas = a % mod;
        while (e > 0) {
            if ((e & 1) != 0) res = res * bas % mod;
            bas = bas * bas % mod;
            e >>= 1;
        }
        return (int)res;
    }
}
