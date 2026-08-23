// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinConnectedGroups(int[][] intervals, int k) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var merged = new List<int[]>();
        foreach (var it in intervals) {
            if (merged.Count == 0 || it[0] > merged[merged.Count - 1][1])
                merged.Add(new int[] { it[0], it[1] });
            else if (it[1] > merged[merged.Count - 1][1])
                merged[merged.Count - 1][1] = it[1];
        }
        int m = merged.Count;
        int ans = m;
        for (int i = 0; i < m; i++) {
            int end = merged[i][1] + k;
            int j = i;
            while (j < m && merged[j][0] <= end) j++;
            int groups = i + 1 + (m - j);
            if (groups < ans) ans = groups;
        }
        return ans;
    }
}
