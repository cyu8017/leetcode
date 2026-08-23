// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int maxIntersectionCount(int[] y) {
        int n = y.length;
        TreeMap<Integer, Integer> line = new TreeMap<>();
        for (int i = 1; i < n; i++) {
            int start = 2 * y[i - 1];
            int end = 2 * y[i];
            if (i != n - 1) {
                if (y[i] > y[i - 1]) end--;
                else end++;
            }
            int a = start, b = end;
            if (a > b) { int t = a; a = b; b = t; }
            line.put(a, line.getOrDefault(a, 0) + 1);
            line.put(b + 1, line.getOrDefault(b + 1, 0) - 1);
        }
        int ans = 0, cur = 0;
        for (int v : line.values()) {
            cur += v;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
