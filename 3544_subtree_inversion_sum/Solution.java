// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    List<Integer>[] graph;
    int[] nums, parent;
    int k;
    Map<String, Long> memo;

    public long subtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = edges.length + 1;
        this.nums = nums;
        this.k = k;
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        parent = new int[n];
        java.util.Arrays.fill(parent, -1);
        memo = new HashMap<>();
        return dp(0, k, false);
    }

    long dp(int u, int steps, boolean inv) {
        String key = u + "," + steps + "," + inv;
        if (memo.containsKey(key)) return memo.get(key);
        long num = nums[u];
        if (inv) num = -num;
        long negNum = -num;
        for (int v : graph[u]) {
            if (v == parent[u]) continue;
            parent[v] = u;
            int ns = steps + 1;
            if (ns > k) ns = k;
            num += dp(v, ns, inv);
            if (steps == k) negNum += dp(v, 1, !inv);
        }
        long res = num;
        if (steps == k && negNum > res) res = negNum;
        memo.put(key, res);
        return res;
    }
}
