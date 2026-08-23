// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumTotalDamage(int[] power) {
        int n = power.Length;
        Array.Sort(power);
        var cnt = new Dictionary<int, int>();
        int[] nxt = new int[n];
        long[] f = new long[n];
        bool[] vis = new bool[n];
        for (int i = 0; i < n; i++) {
            if (!cnt.ContainsKey(power[i])) cnt[power[i]] = 0;
            cnt[power[i]]++;
            nxt[i] = LowerBound(power, power[i] + 3);
        }
        long Dfs(int i) {
            if (i >= n) return 0;
            if (vis[i]) return f[i];
            vis[i] = true;
            long a = Dfs(i + cnt[power[i]]);
            long b = (long)power[i] * cnt[power[i]] + Dfs(nxt[i]);
            return f[i] = Math.Max(a, b);
        }
        return Dfs(0);
    }

    static int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
