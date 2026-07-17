// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

public class Solution {
    private const long MOD = 1000000007L;

    public int[] WaysToFillArray(int[][] queries) {
        var ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
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
                    ways = ways * CombMod(n + exp - 1, exp) % MOD;
                }
                d += d == 2 ? 1 : 2;
            }
            if (value > 1) {
                ways = ways * (n % MOD) % MOD;
            }
            ans[i] = (int)ways;
        }
        return ans;
    }

    private long CombMod(long a, long b) {
        long num = 1;
        long den = 1;
        for (long i = 1; i <= b; i++) {
            num = num * ((a - b + i) % MOD) % MOD;
            den = den * (i % MOD) % MOD;
        }
        return num * PowMod(den, MOD - 2) % MOD;
    }

    private long PowMod(long baseValue, long exp) {
        long result = 1;
        baseValue %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * baseValue % MOD;
            }
            baseValue = baseValue * baseValue % MOD;
            exp >>= 1;
        }
        return result;
    }
}
