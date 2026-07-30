// LeetCode 1499 - Max Value Of Equation
// https://leetcode.com/problems/max-value-of-equation/

using System.Collections.Generic;
public class Solution {
    public int FindMaxValueOfEquation(int[][] points, int k) {
        var q = new LinkedList<(int x, int v)>();
        long ans = long.MinValue / 4;
        foreach (var p in points) {
            int x = p[0], y = p[1];
            while (q.Count > 0 && x - q.First.Value.x > k) q.RemoveFirst();
            if (q.Count > 0) ans = System.Math.Max(ans, (long)x + y + q.First.Value.v);
            int value = y - x;
            while (q.Count > 0 && q.Last.Value.v <= value) q.RemoveLast();
            q.AddLast((x, value));
        }
        return (int)ans;
    }
}
