// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maxStarSum(int[] vals, int[][] edges, int k) {
        int n = vals.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int ans = vals[0];
        for (int i = 0; i < n; i++) {
            List<Integer> neigh = new ArrayList<>();
            for (int v : g[i]) {
                if (vals[v] > 0) neigh.add(vals[v]);
            }
            Collections.sort(neigh, Collections.reverseOrder());
            int sum = vals[i];
            for (int j = 0; j < neigh.size() && j < k; j++) sum += neigh.get(j);
            if (sum > ans) ans = sum;
        }
        return ans;
    }
}
