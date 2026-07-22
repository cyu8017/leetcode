// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

using System;
using System.Collections.Generic;

public class Solution {
    public int VisiblePoints(IList<IList<int>> points, int angle, IList<int> location) {
        int same = 0;
        var a = new List<double>();
        foreach (var p in points) {
            int dx = p[0] - location[0], dy = p[1] - location[1];
            if (dx == 0 && dy == 0) same++;
            else a.Add(Math.Atan2(dy, dx));
        }
        a.Sort();
        var ext = new List<double>(a);
        foreach (double x in a) ext.Add(x + 2 * Math.PI);
        double width = angle * Math.PI / 180.0 + 1e-12;
        int left = 0, best = 0, n = a.Count;
        for (int right = 0; right < ext.Count; right++) {
            while (ext[right] - ext[left] > width) left++;
            best = Math.Max(best, Math.Min(n, right - left + 1));
        }
        return best + same;
    }
}
