// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] SortItems(int n, int m, int[] group, IList<IList<int>> beforeItems) {
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = m;
                m++;
            }
        }

        var itemGraph = new List<int>[n];
        var itemIndeg = new int[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new List<int>();

        var groupGraph = new HashSet<int>[m];
        var groupIndeg = new int[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new HashSet<int>();

        for (int v = 0; v < n; v++) {
            foreach (int u in beforeItems[v]) {
                itemGraph[u].Add(v);
                itemIndeg[v]++;
                if (group[u] != group[v] && groupGraph[group[u]].Add(group[v])) {
                    groupIndeg[group[v]]++;
                }
            }
        }

        List<int> Topo(List<int>[] graph, int[] indeg) {
            var q = new Queue<int>();
            for (int i = 0; i < graph.Length; i++) {
                if (indeg[i] == 0) q.Enqueue(i);
            }
            var order = new List<int>();
            while (q.Count > 0) {
                int u = q.Dequeue();
                order.Add(u);
                foreach (int v in graph[u]) {
                    indeg[v]--;
                    if (indeg[v] == 0) q.Enqueue(v);
                }
            }
            return order.Count == graph.Length ? order : new List<int>();
        }

        var groupAdj = new List<int>[m];
        for (int i = 0; i < m; i++) groupAdj[i] = groupGraph[i].ToList();

        var items = Topo(itemGraph, itemIndeg);
        var groups = Topo(groupAdj, groupIndeg);
        if (items.Count == 0 || groups.Count == 0) return new int[0];

        var buckets = new List<int>[m];
        for (int i = 0; i < m; i++) buckets[i] = new List<int>();
        foreach (int item in items) buckets[group[item]].Add(item);

        var ans = new List<int>();
        foreach (int g in groups) ans.AddRange(buckets[g]);
        return ans.ToArray();
    }
}
