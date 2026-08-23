// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

using System.Collections.Generic;

public class Solution {
    public int BrightestPosition(int[][] lights) {
        var events = new List<(int x, int d)>();
        foreach (var light in lights) {
            int pos = light[0], r = light[1];
            events.Add((pos - r, 1));
            events.Add((pos + r + 1, -1));
        }
        events.Sort((a, b) => a.x != b.x ? a.x.CompareTo(b.x) : b.d.CompareTo(a.d));
        int best = 0, cur = 0, ans = 0;
        foreach (var (x, d) in events) {
            cur += d;
            if (cur > best) { best = cur; ans = x; }
        }
        return ans;
    }
}
