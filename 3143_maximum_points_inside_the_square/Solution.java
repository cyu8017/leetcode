// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int maxPointsInsideSquare(int[][] points, String s) {
        TreeMap<Integer, List<Integer>> g = new TreeMap<>();
        for (int i = 0; i < points.length; i++) {
            int key = Math.max(Math.max(points[i][0], -points[i][0]), Math.max(points[i][1], -points[i][1]));
            g.computeIfAbsent(key, k -> new ArrayList<>()).add(i);
        }
        boolean[] vis = new boolean[26];
        int ans = 0;
        for (Map.Entry<Integer, List<Integer>> e : g.entrySet()) {
            for (int i : e.getValue()) {
                int j = s.charAt(i) - 'a';
                if (vis[j]) return ans;
                vis[j] = true;
            }
            ans += e.getValue().size();
        }
        return ans;
    }
}
