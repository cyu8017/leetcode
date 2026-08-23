// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

using System.Collections.Generic;

public class Solution {
    public int XorAfterQueries(int[] nums, int[][] queries) {
        const int MOD = 1000000007;
        int n = nums.Length;
        var byK = new Dictionary<int, List<(int l, int r, int k, int v)>>();
        foreach (var q in queries) {
            if (!byK.ContainsKey(q[2])) byK[q[2]] = new List<(int, int, int, int)>();
            byK[q[2]].Add((q[0], q[1], q[2], q[3]));
        }
        int[] res = (int[])nums.Clone();
        foreach (var ups in byK.Values) {
            int[] fac = new int[n];
            for (int i = 0; i < n; i++) fac[i] = 1;
            foreach (var u in ups)
                for (int i = u.l; i <= u.r; i += u.k) fac[i] = (int)(1L * fac[i] * u.v % MOD);
            for (int i = 0; i < n; i++) res[i] = (int)(1L * res[i] * fac[i] % MOD);
        }
        int ans = 0;
        foreach (int v in res) ans ^= v;
        return ans;
    }
}
