// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

using System.Collections.Generic;

public class Solution {
    public int MaxIntersectionCount(int[] y) {
        int n = y.Length;
        var line = new SortedDictionary<int, int>();
        for (int i = 1; i < n; i++) {
            int start = 2 * y[i - 1];
            int end = 2 * y[i];
            if (i != n - 1) {
                if (y[i] > y[i - 1]) end--;
                else end++;
            }
            int a = start, b = end;
            if (a > b) { int t = a; a = b; b = t; }
            line.TryGetValue(a, out int va); line[a] = va + 1;
            line.TryGetValue(b + 1, out int vb); line[b + 1] = vb - 1;
        }
        int ans = 0, cur = 0;
        foreach (var kv in line) {
            cur += kv.Value;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
