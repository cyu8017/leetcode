// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinEnergy(int n, int brightness, int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var merged = new List<int[]> { (int[])intervals[0].Clone() };
        for (int i = 1; i < intervals.Length; i++) {
            var x = intervals[i];
            if (merged[merged.Count - 1][1] < x[0]) merged.Add((int[])x.Clone());
            else if (x[1] > merged[merged.Count - 1][1]) merged[merged.Count - 1][1] = x[1];
        }
        long ans = 0;
        foreach (var interval in merged) {
            int m = interval[1] - interval[0] + 1;
            ans += (long)((brightness + 2) / 3) * m;
        }
        return ans;
    }
}
