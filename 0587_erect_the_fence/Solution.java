// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[][] outerTrees(int[][] trees) {
        int[][] points = Arrays.copyOf(trees, trees.length);
        Arrays.sort(points, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        if (points.length <= 1) {
            return points;
        }

        List<int[]> lower = build(points);
        int[][] reversed = new int[points.length][];
        for (int i = 0; i < points.length; ++i) {
            reversed[i] = points[points.length - 1 - i];
        }
        List<int[]> upper = build(reversed);

        Set<String> seen = new HashSet<>();
        List<int[]> unique = new ArrayList<>();
        for (int i = 0; i + 1 < lower.size(); ++i) {
            addUnique(unique, seen, lower.get(i));
        }
        for (int i = 0; i + 1 < upper.size(); ++i) {
            addUnique(unique, seen, upper.get(i));
        }
        return unique.toArray(new int[0][]);
    }

    private List<int[]> build(int[][] ordered) {
        List<int[]> hull = new ArrayList<>();
        for (int[] point : ordered) {
            while (hull.size() >= 2 && cross(hull.get(hull.size() - 2), hull.get(hull.size() - 1), point) < 0) {
                hull.remove(hull.size() - 1);
            }
            hull.add(point);
        }
        return hull;
    }

    private long cross(int[] o, int[] a, int[] b) {
        return 1L * (a[0] - o[0]) * (b[1] - o[1]) - 1L * (a[1] - o[1]) * (b[0] - o[0]);
    }

    private void addUnique(List<int[]> unique, Set<String> seen, int[] point) {
        String key = point[0] + "," + point[1];
        if (seen.add(key)) {
            unique.add(point);
        }
    }
}
