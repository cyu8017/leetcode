// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

import java.util.*;

class Solution {
    private List<Integer>[] graph;
    private int[] count;
    private int[] ans;
    private int n;

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        this.n = n;
        graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        count = new int[n];
        ans = new int[n];
        Arrays.fill(count, 1);
        post(0, -1);
        reroot(0, -1);
        return ans;
    }

    private void post(int node, int parent) {
        for (int child : graph[node]) {
            if (child == parent) continue;
            post(child, node);
            count[node] += count[child];
            ans[node] += ans[child] + count[child];
        }
    }

    private void reroot(int node, int parent) {
        for (int child : graph[node]) {
            if (child == parent) continue;
            ans[child] = ans[node] - count[child] + (n - count[child]);
            reroot(child, node);
        }
    }
}
