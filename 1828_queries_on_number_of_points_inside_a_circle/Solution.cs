// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

public class Solution {
    public int[] CountPoints(int[][] points, int[][] queries) {
        int[] result = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int xq = queries[qi][0], yq = queries[qi][1], r = queries[qi][2];
            int radiusSq = r * r;
            int count = 0;
            foreach (var point in points) {
                int dx = point[0] - xq, dy = point[1] - yq;
                if (dx * dx + dy * dy <= radiusSq) count++;
            }
            result[qi] = count;
        }
        return result;
    }
}
