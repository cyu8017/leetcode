// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

using System.Collections.Generic;

public class Solution {
    public int[] SumOfDistancesInTree(int n, int[][] edges) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) { graph[e[0]].Add(e[1]); graph[e[1]].Add(e[0]); }
        int[] count = new int[n], ans = new int[n];
        for (int i = 0; i < n; i++) count[i] = 1;
        void Post(int node, int parent) {
            foreach (int child in graph[node]) {
                if (child == parent) continue;
                Post(child, node);
                count[node] += count[child];
                ans[node] += ans[child] + count[child];
            }
        }
        void Reroot(int node, int parent) {
            foreach (int child in graph[node]) {
                if (child == parent) continue;
                ans[child] = ans[node] - count[child] + (n - count[child]);
                Reroot(child, node);
            }
        }
        Post(0, -1);
        Reroot(0, -1);
        return ans;
    }
}
