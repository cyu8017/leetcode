// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] restoreArray(int[][] adjacentPairs) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] pair : adjacentPairs) {
            graph.computeIfAbsent(pair[0], key -> new ArrayList<>()).add(pair[1]);
            graph.computeIfAbsent(pair[1], key -> new ArrayList<>()).add(pair[0]);
        }
        int start = 0;
        for (int[] pair : adjacentPairs) {
            if (graph.get(pair[0]).size() == 1) {
                start = pair[0];
                break;
            }
            if (graph.get(pair[1]).size() == 1) {
                start = pair[1];
                break;
            }
        }
        int n = graph.size();
        int[] ans = new int[n];
        ans[0] = start;
        Integer prev = null;
        for (int i = 1; i < n; i++) {
            int cur = ans[i - 1];
            List<Integer> neighbors = graph.get(cur);
            int nxt = (prev == null || neighbors.get(0) != (int) prev) ? neighbors.get(0) : neighbors.get(1);
            ans[i] = nxt;
            prev = cur;
        }
        return ans;
    }
}
