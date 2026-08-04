// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

import java.util.*;

class Solution {
    public List<Integer> shortestDistanceColor(int[] colors, int[][] queries) {
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < colors.length; i++) {
            pos.computeIfAbsent(colors[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int i = q[0], c = q[1];
            if (!pos.containsKey(c)) { ans.add(-1); continue; }
            List<Integer> arr = pos.get(c);
            int idx = Collections.binarySearch(arr, i);
            if (idx < 0) idx = -idx - 1;
            int best = Integer.MAX_VALUE;
            if (idx < arr.size()) best = Math.min(best, arr.get(idx) - i);
            if (idx > 0) best = Math.min(best, i - arr.get(idx - 1));
            ans.add(best == Integer.MAX_VALUE ? -1 : best);
        }
        return ans;
    }
}
