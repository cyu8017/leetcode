// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int RectangleArea(int[][] rectangles) {
        const int MOD = 1_000_000_007;
        var events = new List<(int x, int typ, int y1, int y2)>();
        foreach (var r in rectangles) {
            events.Add((r[0], 1, r[1], r[3]));
            events.Add((r[2], -1, r[1], r[3]));
        }
        events.Sort((a, b) => a.x.CompareTo(b.x));

        int CoveredLength(List<(int, int)> active) {
            if (active.Count == 0) return 0;
            active.Sort((a, b) => a.Item1.CompareTo(b.Item1));
            int total = 0, curStart = active[0].Item1, curEnd = active[0].Item2;
            for (int i = 1; i < active.Count; i++) {
                int start = active[i].Item1, end = active[i].Item2;
                if (start > curEnd) {
                    total += curEnd - curStart;
                    curStart = start;
                    curEnd = end;
                } else curEnd = Math.Max(curEnd, end);
            }
            total += curEnd - curStart;
            return total;
        }

        var activeSegs = new List<(int, int)>();
        long area = 0;
        int prevX = events[0].x;
        foreach (var (x, typ, y1, y2) in events) {
            area += (long)CoveredLength(new List<(int, int)>(activeSegs)) * (x - prevX);
            if (typ == 1) activeSegs.Add((y1, y2));
            else activeSegs.Remove((y1, y2));
            prevX = x;
        }
        return (int)(area % MOD);
    }
}
