// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] result = new int[queries.length];
        for (int queryIndex = 0; queryIndex < queries.length; queryIndex++) {
            int xq = queries[queryIndex][0];
            int yq = queries[queryIndex][1];
            int r = queries[queryIndex][2];
            long radiusSq = (long) r * r;
            int count = 0;
            for (int[] point : points) {
                int x = point[0];
                int y = point[1];
                long dx = x - xq;
                long dy = y - yq;
                if (dx * dx + dy * dy <= radiusSq) {
                    count++;
                }
            }
            result[queryIndex] = count;
        }
        return result;
    }
}
