// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] FindMaximalUncoveredRanges(int n, int[][] ranges) {
        Array.Sort(ranges, (a, b) => a[0].CompareTo(b[0]));
        var ans = new List<int[]>();
        int cur = 0;
        foreach (var r in ranges) {
            if (r[0] > cur) ans.Add(new int[] { cur, r[0] - 1 });
            if (r[1] + 1 > cur) cur = r[1] + 1;
        }
        if (cur < n) ans.Add(new int[] { cur, n - 1 });
        return ans.ToArray();
    }
}
