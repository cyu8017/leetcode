// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

import java.util.Arrays;

class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        int ans = 0;
        for (int i = 0; i < points.length; i++) {
            int y1 = points[i][1];
            int maxY = Integer.MIN_VALUE;
            for (int j = i + 1; j < points.length; j++) {
                int y2 = points[j][1];
                if (maxY < y2 && y2 <= y1) {
                    maxY = y2;
                    ans++;
                }
            }
        }
        return ans;
    }
}
