// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

public class Solution {
    const int MX = 100001;
    const long MOD = 1000000007;
    static long[] _pw;

    static long[] Pow10() {
        if (_pw != null) return _pw;
        _pw = new long[MX];
        _pw[0] = 1;
        for (int i = 1; i < MX; i++) _pw[i] = _pw[i - 1] * 10 % MOD;
        return _pw;
    }

    public int[] SumAndMultiply(string s, int[][] queries) {
        int n = s.Length;
        int[] sumD = new int[n + 1], cntN0 = new int[n + 1];
        long[] p = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            long d = s[i - 1] - '0';
            sumD[i] = sumD[i - 1] + (int)d;
            cntN0[i] = cntN0[i - 1];
            if (d > 0) {
                cntN0[i]++;
                p[i] = (p[i - 1] * 10 + d) % MOD;
            } else p[i] = p[i - 1];
        }
        long[] pw = Pow10();
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int l = queries[i][0], r = queries[i][1];
            int n0 = cntN0[r + 1] - cntN0[l];
            long sd = sumD[r + 1] - sumD[l];
            long x = (p[r + 1] - p[l] * pw[n0] % MOD + MOD) % MOD;
            ans[i] = (int)(x * sd % MOD);
        }
        return ans;
    }
}
