// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

using System.Collections.Generic;

public class Solution {
    public int CountLatticePoints(int[][] circles) {
        var seen = new HashSet<(int, int)>();
        foreach (var c in circles) {
            int x = c[0], y = c[1], r = c[2];
            for (int i = x - r; i <= x + r; i++)
                for (int j = y - r; j <= y + r; j++)
                    if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
                        seen.Add((i, j));
        }
        return seen.Count;
    }
}
