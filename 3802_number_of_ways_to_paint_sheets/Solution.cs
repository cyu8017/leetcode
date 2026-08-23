// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

using System;
using System.Collections.Generic;

public class Solution {
    public int NumberOfWays(int n, int[] limit) {
        const long MOD = 1000000007;
        Array.Sort(limit);
        var points = new List<int> { 1, n };
        foreach (int x in limit) {
            if (x + 1 > 1 && x + 1 < n) points.Add(x + 1);
            if (n - x > 1 && n - x < n) points.Add(n - x);
        }
        points.Sort();
        int pu = 0;
        for (int i = 0; i < points.Count; i++) {
            if (i == 0 || points[i] != points[i - 1]) points[pu++] = points[i];
        }
        points.RemoveRange(pu, points.Count - pu);
        long CountGE(int x) {
            int lo = 0, hi = limit.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (limit[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return limit.Length - lo;
        }
        long ans = 0;
        for (int i = 0; i + 1 < points.Count; i++) {
            int x = points[i];
            long a = CountGE(x), b = CountGE(n - x);
            long same = CountGE(Math.Max(x, n - x));
            long ways = (a * b - same) % MOD;
            long length = points[i + 1] - x;
            ans = (ans + ways * length) % MOD;
        }
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
}
