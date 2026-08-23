// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FilterOccupiedIntervals(int[][] occupiedIntervals, int freeStart, int freeEnd) {
        Array.Sort(occupiedIntervals, (a, b) => a[0].CompareTo(b[0]));
        var busy = new List<int[]> { (int[])occupiedIntervals[0].Clone() };
        for (int i = 1; i < occupiedIntervals.Length; i++) {
            var cur = occupiedIntervals[i];
            var last = busy[busy.Count - 1];
            if (last[1] + 1 < cur[0]) busy.Add((int[])cur.Clone());
            else if (cur[1] > last[1]) last[1] = cur[1];
        }
        var ans = new List<IList<int>>();
        foreach (var it in busy) {
            int s = it[0], e = it[1];
            if (e < freeStart || s > freeEnd) ans.Add(new List<int> { s, e });
            else {
                if (s < freeStart) ans.Add(new List<int> { s, freeStart - 1 });
                if (e > freeEnd) ans.Add(new List<int> { freeEnd + 1, e });
            }
        }
        return ans;
    }
}
