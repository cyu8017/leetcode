// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

using System.Collections.Generic;

public class Solution {
    public int[] LeftmostBuildingQueries(int[] heights, int[][] queries) {
        int qn = queries.Length;
        int[] ans = new int[qn];
        for (int i = 0; i < qn; i++) ans[i] = -1;
        var buckets = new List<(int h, int qi)>[heights.Length];
        for (int i = 0; i < heights.Length; i++) buckets[i] = new List<(int, int)>();
        for (int qi = 0; qi < qn; qi++) {
            int a = queries[qi][0], b = queries[qi][1];
            if (a > b) { int t = a; a = b; b = t; }
            if (a == b || heights[a] < heights[b]) {
                ans[qi] = b;
                continue;
            }
            buckets[b].Add((heights[a], qi));
        }
        var st = new List<(int h, int i)>();
        for (int i = heights.Length - 1; i >= 0; i--) {
            foreach (var (h, qi) in buckets[i]) {
                int lo = 0, hi = st.Count - 1, pos = -1;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (st[mid].h > h) {
                        pos = st[mid].i;
                        lo = mid + 1;
                    } else hi = mid - 1;
                }
                ans[qi] = pos;
            }
            while (st.Count > 0 && st[st.Count - 1].h <= heights[i]) st.RemoveAt(st.Count - 1);
            st.Add((heights[i], i));
        }
        return ans;
    }
}
