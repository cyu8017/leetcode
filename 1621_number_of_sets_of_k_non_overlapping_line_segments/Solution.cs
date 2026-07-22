// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

public class Solution {
    private const int MOD = 1000000007;

    public int NumberOfSets(int n, int k) {
        return (int)CombMod(n + k - 1, 2 * k);
    }

    private static long CombMod(int n, int r) {
        if (r < 0 || r > n) return 0;
        long num = 1, den = 1;
        for (int i = 0; i < r; i++) {
            num = num * (n - i) % MOD;
            den = den * (i + 1) % MOD;
        }
        return num * ModPow(den, MOD - 2) % MOD;
    }

    private static long ModPow(long baseVal, long exp) {
        long r = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) r = r * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return r;
    }
}
