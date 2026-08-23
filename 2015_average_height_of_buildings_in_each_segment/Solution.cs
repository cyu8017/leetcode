// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] AverageHeightOfBuildings(int[][] buildings) {
        var events = new List<int[]>();
        foreach (var b in buildings) {
            events.Add(new[] { b[0], 1, b[2] });
            events.Add(new[] { b[1], -1, b[2] });
        }
        events.Sort((a, b) => a[0] != b[0] ? a[0].CompareTo(b[0]) : a[1].CompareTo(b[1]));
        var ans = new List<int[]>();
        int count = 0, sum = 0, prev = events[0][0];
        foreach (var e in events) {
            if (e[0] != prev && count > 0) {
                int avg = sum / count;
                if (ans.Count > 0 && ans[ans.Count - 1][1] == prev && ans[ans.Count - 1][2] == avg)
                    ans[ans.Count - 1][1] = e[0];
                else ans.Add(new[] { prev, e[0], avg });
            }
            count += e[1];
            sum += e[1] * e[2];
            prev = e[0];
        }
        return ans.ToArray();
    }
}
