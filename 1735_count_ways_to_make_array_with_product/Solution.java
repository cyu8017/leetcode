// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

class Solution {
    private static final long MOD = 1_000_000_007L;

    public int[] waysToFillArray(int[][] queries) {
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long n = queries[i][0];
            long value = queries[i][1];
            long ways = 1;
            long d = 2;
            while (d * d <= value) {
                if (value % d == 0) {
                    long exp = 0;
                    while (value % d == 0) {
                        value /= d;
                        exp++;
                    }
                    ways = ways * combMod(n + exp - 1, exp) % MOD;
                }
                d += d == 2 ? 1 : 2;
            }
            if (value > 1) {
                ways = ways * (n % MOD) % MOD;
            }
            ans[i] = (int) ways;
        }
        return ans;
    }

    private long combMod(long a, long b) {
        long num = 1;
        long den = 1;
        for (long i = 1; i <= b; i++) {
            num = num * ((a - b + i) % MOD) % MOD;
            den = den * (i % MOD) % MOD;
        }
        return num * powMod(den, MOD - 2) % MOD;
    }

    private long powMod(long base, long exp) {
        long result = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        return result;
    }
}
