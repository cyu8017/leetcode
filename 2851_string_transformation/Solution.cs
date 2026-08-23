// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

public class Solution {
    const int MOD = 1000000007;

    int ModPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return (int)res;
    }

    public int NumberOfWays(string s, string t, long k) {
        int n = s.Length;
        string ss = s + s;
        if (ss.Substring(0, 2 * n - 1).IndexOf(t, System.StringComparison.Ordinal) < 0) return 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) if (ss.Substring(i, n) == t) cnt++;
        int same = s == t ? 1 : 0;
        int pk = ModPow(n - 1, k);
        int invn = ModPow(n, MOD - 2);
        int sign = (k % 2 == 1) ? MOD - 1 : 1;
        int waysSame = (int)((1L * pk + 1L * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD);
        int waysDiff = (int)((1L * pk - sign + MOD) % MOD * invn % MOD);
        if (same == 1) return waysSame;
        return (int)(1L * waysDiff * cnt % MOD);
    }
}
