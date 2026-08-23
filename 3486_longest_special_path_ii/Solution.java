// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private List<int[]>[] g;
    private int[] nums;
    private int bestLen, bestNodes;

    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        this.nums = nums;
        int n = nums.length;
        @SuppressWarnings("unchecked")
        List<int[]>[] gg = new ArrayList[n];
        g = gg;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[]{e[1], e[2]});
            g[e[1]].add(new int[]{e[0], e[2]});
        }
        bestLen = 0;
        bestNodes = 1;
        dfs(0, -1, 0, new ArrayList<>(), new ArrayList<>());
        return new int[]{bestLen, bestNodes};
    }

    private void dfs(int u, int p, int dist, List<Integer> pathVals, List<Integer> pathDist) {
        pathVals.add(nums[u]);
        pathDist.add(dist);
        Map<Integer, Integer> freq = new HashMap<>();
        int dups = 0, left = 0;
        for (int right = 0; right < pathVals.size(); right++) {
            int v = pathVals.get(right);
            freq.merge(v, 1, Integer::sum);
            if (freq.get(v) == 2) dups++;
            while (dups > 1) {
                int lv = pathVals.get(left);
                if (freq.get(lv) == 2) dups--;
                freq.put(lv, freq.get(lv) - 1);
                left++;
            }
        }
        int length = dist - pathDist.get(left);
        int nodes = pathVals.size() - left;
        if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (int[] e : g[u]) {
            if (e[0] == p) continue;
            dfs(e[0], u, dist + e[1], pathVals, pathDist);
        }
        pathVals.remove(pathVals.size() - 1);
        pathDist.remove(pathDist.size() - 1);
    }
}
