// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

import java.util.*;

class Solution {
    private Map<Integer, List<Integer>> g;
    private List<Integer> path;

    private void dfs(int u) {
        List<Integer> nbrs = g.computeIfAbsent(u, k -> new ArrayList<>());
        while (!nbrs.isEmpty()) {
            int v = nbrs.remove(nbrs.size() - 1);
            dfs(v);
        }
        path.add(u);
    }

    public int[][] validArrangement(int[][] pairs) {
        g = new HashMap<>();
        Map<Integer, Integer> indeg = new HashMap<>();
        Map<Integer, Integer> outdeg = new HashMap<>();
        for (int[] p : pairs) {
            int u = p[0], v = p[1];
            g.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            outdeg.put(u, outdeg.getOrDefault(u, 0) + 1);
            indeg.put(v, indeg.getOrDefault(v, 0) + 1);
        }
        int start = pairs[0][0];
        for (Map.Entry<Integer, Integer> kv : outdeg.entrySet()) {
            if (kv.getValue() - indeg.getOrDefault(kv.getKey(), 0) == 1) {
                start = kv.getKey();
                break;
            }
        }
        path = new ArrayList<>();
        dfs(start);
        Collections.reverse(path);
        int[][] ans = new int[path.size() - 1][2];
        for (int i = 0; i + 1 < path.size(); i++) {
            ans[i][0] = path.get(i);
            ans[i][1] = path.get(i + 1);
        }
        return ans;
    }
}
