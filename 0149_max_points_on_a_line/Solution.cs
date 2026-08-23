// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

using System;
using System.Collections.Generic;
public class Solution {
    public int MaxPoints(int[][] points) {
        var best = 0;
        for (var i = 0; i < points.Length; i++) {
            var slopes = new Dictionary<(int, int), int>(); var local = 1;
            for (var j = i + 1; j < points.Length; j++) {
                var dx = points[j][0] - points[i][0]; var dy = points[j][1] - points[i][1];
                var divisor = Gcd(dx, dy); dx /= divisor; dy /= divisor;
                if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
                var key = (dx, dy); slopes[key] = slopes.GetValueOrDefault(key) + 1;
                local = Math.Max(local, slopes[key] + 1);
            }
            best = Math.Max(best, local);
        }
        return best;
    }
    private int Gcd(int a, int b) { a = Math.Abs(a); b = Math.Abs(b); while (b != 0) { var temp = a % b; a = b; b = temp; } return a; }
}