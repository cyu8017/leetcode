// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int maxBuilding(int n, int[] restrictions) {
        return maxBuilding(n, new int[0][]);
    }

    public int maxBuilding(int n, int[][] restrictions) {
        List<int[]> points = new ArrayList<>();
        points.add(new int[] {1, 0});
        for (int[] restriction : restrictions) {
            points.add(new int[] {restriction[0], restriction[1]});
        }
        points.sort(Comparator.comparingInt(point -> point[0]));
        if (points.get(points.size() - 1)[0] != n) {
            points.add(new int[] {n, n - 1});
        }

        for (int i = 1; i < points.size(); i++) {
            int[] prev = points.get(i - 1);
            int[] curr = points.get(i);
            curr[1] = Math.min(curr[1], prev[1] + curr[0] - prev[0]);
        }

        for (int i = points.size() - 2; i >= 0; i--) {
            int[] next = points.get(i + 1);
            int[] curr = points.get(i);
            curr[1] = Math.min(curr[1], next[1] + next[0] - curr[0]);
        }

        int best = 0;
        for (int[] point : points) {
            best = Math.max(best, point[1]);
        }
        for (int i = 0; i < points.size() - 1; i++) {
            int[] left = points.get(i);
            int[] right = points.get(i + 1);
            best = Math.max(best, (left[1] + right[1] + right[0] - left[0]) / 2);
        }

        return best;
    }
}
