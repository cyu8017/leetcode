// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinGroups(int[][] intervals) {
        var events = new List<(int t, int d)>();
        foreach (var it in intervals) {
            events.Add((it[0], 1));
            events.Add((it[1] + 1, -1));
        }
        events.Sort();
        int cur = 0, ans = 0;
        foreach (var (_, d) in events) {
            cur += d;
            ans = Math.Max(ans, cur);
        }
        return ans;
    }
}
