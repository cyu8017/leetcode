// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public long PopcountDepth(long n, int k) {
        if (k == 0) return n >= 1 ? 1 : 0;
        int Depth(int x) {
            if (x <= 0) return 100;
            int d = 0;
            while (x > 1) {
                x = BitOperations.PopCount((uint)x);
                d++;
            }
            return d;
        }
        string s = "";
        for (long x = n; x > 0; x >>= 1) s = ((x & 1) == 1 ? "1" : "0") + s;
        if (s.Length == 0) s = "0";
        var memo = new Dictionary<(int, int, int, int), long>();
        long Dfs(int pos, int tight, int started, int pc) {
            if (pos == s.Length) {
                if (started == 0) return 0;
                if (pc == 1) return k == 1 ? 1 : 0;
                return Depth(pc) == k - 1 ? 1 : 0;
            }
            var key = (pos, tight, started, pc);
            if (memo.ContainsKey(key)) return memo[key];
            int up = tight == 1 ? s[pos] - '0' : 1;
            long res = 0;
            for (int dig = 0; dig <= up; dig++) {
                int nt = (tight == 1 && dig == up) ? 1 : 0;
                if (started == 0 && dig == 0) res += Dfs(pos + 1, nt, 0, 0);
                else res += Dfs(pos + 1, nt, 1, pc + dig);
            }
            return memo[key] = res;
        }
        return Dfs(0, 1, 0, 0);
    }
}
