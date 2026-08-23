// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

using System.Collections.Generic;

public class Solution {
    public int CountCoveredBuildings(int n, int[][] buildings) {
        var g1 = new Dictionary<int, List<int>>();
        var g2 = new Dictionary<int, List<int>>();
        foreach (var b in buildings) {
            if (!g1.ContainsKey(b[0])) g1[b[0]] = new List<int>();
            if (!g2.ContainsKey(b[1])) g2[b[1]] = new List<int>();
            g1[b[0]].Add(b[1]);
            g2[b[1]].Add(b[0]);
        }
        foreach (var list in g1.Values) list.Sort();
        foreach (var list in g2.Values) list.Sort();
        int ans = 0;
        foreach (var b in buildings) {
            int x = b[0], y = b[1];
            var l1 = g1[x];
            var l2 = g2[y];
            if (l2[0] < x && x < l2[l2.Count - 1] && l1[0] < y && y < l1[l1.Count - 1]) ans++;
        }
        return ans;
    }
}
