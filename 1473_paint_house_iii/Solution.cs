// LeetCode 1473 - Paint House Iii
// https://leetcode.com/problems/paint-house-iii/

using System.Collections.Generic;
public class Solution {
    public int MinCost(int[] houses, int[][] cost, int m, int n, int target) {
        long inf = 1000000000000000L;
        var dp = new Dictionary<(int,int), long> { [(0, 0)] = 0 };
        for (int i = 0; i < houses.Length; i++) {
            var nxt = new Dictionary<(int,int), long>();
            var colors = houses[i] != 0 ? new[] { houses[i] } : EnumerableRange(1, n);
            foreach (var kv in dp) {
                int prev = kv.Key.Item1, groups = kv.Key.Item2; long value = kv.Value;
                foreach (int color in colors) {
                    int ng = groups + (color != prev ? 1 : 0);
                    if (ng <= target) {
                        long nv = value + (houses[i] != 0 ? 0 : cost[i][color - 1]);
                        var key = (color, ng);
                        if (!nxt.ContainsKey(key) || nv < nxt[key]) nxt[key] = nv;
                    }
                }
            }
            dp = nxt;
        }
        long ans = inf;
        foreach (var kv in dp) if (kv.Key.Item2 == target) ans = System.Math.Min(ans, kv.Value);
        return ans == inf ? -1 : (int)ans;
    }
    int[] EnumerableRange(int start, int count) {
        var a = new int[count]; for (int i = 0; i < count; i++) a[i] = start + i; return a;
    }
}
