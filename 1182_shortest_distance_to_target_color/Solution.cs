// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ShortestDistanceColor(int[] colors, int[][] queries) {
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < colors.Length; i++) {
            if (!pos.ContainsKey(colors[i])) pos[colors[i]] = new List<int>();
            pos[colors[i]].Add(i);
        }

        var ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int idx = queries[i][0], c = queries[i][1];
            if (!pos.ContainsKey(c)) {
                ans[i] = -1;
                continue;
            }
            var arr = pos[c];
            int lo = 0, hi = arr.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid] < idx) lo = mid + 1;
                else hi = mid;
            }
            int best = int.MaxValue;
            if (lo < arr.Count) best = Math.Min(best, arr[lo] - idx);
            if (lo > 0) best = Math.Min(best, idx - arr[lo - 1]);
            ans[i] = best == int.MaxValue ? -1 : best;
        }
        return ans;
    }
}
