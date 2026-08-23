// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] EmployeeFreeTime(int[][][] schedule) {
        var intervals = new List<int[]>();
        foreach (var employee in schedule)
            foreach (var item in employee)
                intervals.Add(new[] { item[0], item[1] });
        intervals.Sort((a, b) => a[0].CompareTo(b[0]));
        var merged = new List<int[]>();
        foreach (var iv in intervals) {
            if (merged.Count == 0 || merged[merged.Count - 1][1] < iv[0]) merged.Add(iv);
            else merged[merged.Count - 1][1] = Math.Max(merged[merged.Count - 1][1], iv[1]);
        }
        var result = new List<int[]>();
        for (int i = 1; i < merged.Count; i++)
            result.Add(new[] { merged[i - 1][1], merged[i][0] });
        return result.ToArray();
    }
}
