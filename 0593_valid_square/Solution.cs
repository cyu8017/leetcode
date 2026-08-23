// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

using System;

public class Solution {
    public bool ValidSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] points = { p1, p2, p3, p4 };
        var distances = new int[6];
        int idx = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = i + 1; j < 4; ++j) {
                distances[idx++] = DistSq(points[i], points[j]);
            }
        }
        Array.Sort(distances);
        return distances[0] > 0 && distances[0] == distances[1] && distances[1] == distances[2] &&
               distances[2] == distances[3] && distances[4] == distances[5] &&
               distances[4] == 2 * distances[0];
    }

    private int DistSq(int[] a, int[] b) {
        int dx = a[0] - b[0], dy = a[1] - b[1];
        return dx * dx + dy * dy;
    }
}
