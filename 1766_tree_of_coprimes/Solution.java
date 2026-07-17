// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class Solution {
    private List<List<Integer>> adj;
    private int[] nums;
    private int[] ans;
    private List<Deque<int[]>> path;

    public int[] getCoprimes(int[] nums, int[][] edges) {
        int n = nums.length;
        this.nums = nums;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        ans = new int[n];
        java.util.Arrays.fill(ans, -1);
        path = new ArrayList<>();
        for (int v = 0; v <= 50; v++) {
            path.add(new ArrayDeque<>());
        }
        dfs(0, -1, 0);
        return ans;
    }

    private void dfs(int node, int parent, int depth) {
        int bestDepth = -1;
        int bestNode = -1;
        int val = nums[node];
        for (int d = 1; d <= 50; d++) {
            if (gcd(val, d) == 1 && !path.get(d).isEmpty()) {
                int[] cand = path.get(d).peek();
                if (cand[0] > bestDepth) {
                    bestDepth = cand[0];
                    bestNode = cand[1];
                }
            }
        }
        ans[node] = bestNode;
        path.get(val).push(new int[] { depth, node });
        for (int nxt : adj.get(node)) {
            if (nxt != parent) {
                dfs(nxt, node, depth + 1);
            }
        }
        path.get(val).pop();
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
