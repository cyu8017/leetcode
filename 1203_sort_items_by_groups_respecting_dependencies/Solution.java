// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

import java.util.*;

class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) group[i] = m++;
        }
        List<Integer>[] itemGraph = new List[n];
        int[] itemIndeg = new int[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new ArrayList<>();
        List<Integer>[] groupGraph = new List[m];
        int[] groupIndeg = new int[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new ArrayList<>();
        Set<Long> seenGroupEdge = new HashSet<>();
        for (int v = 0; v < n; v++) {
            for (int u : beforeItems.get(v)) {
                itemGraph[u].add(v);
                itemIndeg[v]++;
                if (group[u] != group[v]) {
                    long key = ((long) group[u] << 32) | group[v];
                    if (seenGroupEdge.add(key)) {
                        groupGraph[group[u]].add(group[v]);
                        groupIndeg[group[v]]++;
                    }
                }
            }
        }
        List<Integer> items = topo(itemGraph, itemIndeg);
        List<Integer> groups = topo(groupGraph, groupIndeg);
        if (items.isEmpty() || groups.isEmpty()) return new int[0];
        List<Integer>[] buckets = new List[m];
        for (int i = 0; i < m; i++) buckets[i] = new ArrayList<>();
        for (int item : items) buckets[group[item]].add(item);
        List<Integer> ans = new ArrayList<>();
        for (int g : groups) ans.addAll(buckets[g]);
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) result[i] = ans.get(i);
        return result;
    }
    private List<Integer> topo(List<Integer>[] graph, int[] indeg) {
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < indeg.length; i++) if (indeg[i] == 0) q.offer(i);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : graph[u]) if (--indeg[v] == 0) q.offer(v);
        }
        return order.size() == graph.length ? order : List.of();
    }
}
