// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

using System.Collections.Generic;

public class Solution {
    public int CountTrapezoids(int[][] points) {
        const int mod = 1000000007;
        var cnt = new Dictionary<int, int>();
        foreach (var p in points) {
            if (!cnt.ContainsKey(p[1])) cnt[p[1]] = 0;
            cnt[p[1]]++;
        }
        long ans = 0, s = 0;
        foreach (var kv in cnt) {
            long t = 1L * kv.Value * (kv.Value - 1) / 2;
            ans = (ans + s * t) % mod;
            s += t;
        }
        return (int)ans;
    }
}
