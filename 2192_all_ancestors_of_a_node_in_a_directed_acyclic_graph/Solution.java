// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

import java.util.*;

class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        int[] indeg = new int[n];
        for (int[] e : edges) { g[e[0]].add(e[1]); indeg[e[1]]++; }
        TreeSet<Integer>[] anc = new TreeSet[n];
        for (int i = 0; i < n; i++) anc[i] = new TreeSet<>();
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g[u]) {
                anc[v].add(u);
                anc[v].addAll(anc[u]);
                if (--indeg[v] == 0) q.offer(v);
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) ans.add(new ArrayList<>(anc[i]));
        return ans;
    }
}
