// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

public class Solution {
    public IList<IList<int>> GetAncestors(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        int[] indeg = new int[n];
        foreach (var e in edges) { g[e[0]].Add(e[1]); indeg[e[1]]++; }
        var anc = new SortedSet<int>[n];
        for (int i = 0; i < n; i++) anc[i] = new SortedSet<int>();
        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g[u]) {
                anc[v].Add(u);
                foreach (int a in anc[u]) anc[v].Add(a);
                if (--indeg[v] == 0) q.Enqueue(v);
            }
        }
        var ans = new List<IList<int>>();
        for (int i = 0; i < n; i++) ans.Add(anc[i].ToList());
        return ans;
    }
}
