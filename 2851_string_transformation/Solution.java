// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

class Solution {
    private static final int MOD = 1000000007;

    public int numberOfWays(String s, String t, long k) {
        int n = s.length();
        String ss = s + s;
        if (ss.substring(0, 2 * n - 1).indexOf(t) < 0) return 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) if (ss.substring(i, i + n).equals(t)) cnt++;
        boolean same = s.equals(t);
        int pk = modPow(n - 1, k);
        int invn = modPow(n, MOD - 2);
        int sign = (k % 2 == 1) ? MOD - 1 : 1;
        int waysSame = (int) ((1L * pk + 1L * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD);
        int waysDiff = (int) ((1L * pk - sign + MOD) % MOD * invn % MOD);
        if (same) return waysSame;
        return (int) (1L * waysDiff * cnt % MOD);
    }

    private int modPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return (int) res;
    }
}
