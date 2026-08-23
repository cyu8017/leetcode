// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] OuterTrees(int[][] trees) {
        var points = trees.OrderBy(p => p[0]).ThenBy(p => p[1]).ToArray();
        if (points.Length <= 1) return points;

        List<int[]> Build(IEnumerable<int[]> ordered) {
            var hull = new List<int[]>();
            foreach (var point in ordered) {
                while (hull.Count >= 2 && Cross(hull[^2], hull[^1], point) < 0) {
                    hull.RemoveAt(hull.Count - 1);
                }
                hull.Add(point);
            }
            return hull;
        }

        var lower = Build(points);
        var upper = Build(points.Reverse());
        var unique = new HashSet<string>();
        var result = new List<int[]>();
        void AddUnique(IList<int[]> hull) {
            for (int i = 0; i + 1 < hull.Count; ++i) {
                string key = hull[i][0] + "," + hull[i][1];
                if (unique.Add(key)) result.Add(hull[i]);
            }
        }
        AddUnique(lower);
        AddUnique(upper);
        return result.ToArray();
    }

    private long Cross(int[] o, int[] a, int[] b) {
        return 1L * (a[0] - o[0]) * (b[1] - o[1]) - 1L * (a[1] - o[1]) * (b[0] - o[0]);
    }
}
