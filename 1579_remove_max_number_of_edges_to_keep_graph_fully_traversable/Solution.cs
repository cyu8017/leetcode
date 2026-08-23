// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

public class Solution {
    private class DSU {
        private readonly int[] parent;
        public int Components;
        public DSU(int n) {
            parent = new int[n + 1];
            for (int i = 0; i <= n; i++) parent[i] = i;
            Components = n;
        }
        public int Find(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        public bool Union(int a, int b) {
            a = Find(a); b = Find(b);
            if (a == b) return false;
            parent[a] = b;
            Components--;
            return true;
        }
    }

    public int MaxNumEdgesToRemove(int n, int[][] edges) {
        var alice = new DSU(n);
        var bob = new DSU(n);
        int used = 0;
        foreach (var e in edges) {
            if (e[0] == 3) {
                bool merged = alice.Union(e[1], e[2]);
                bob.Union(e[1], e[2]);
                if (merged) used++;
            }
        }
        foreach (var e in edges) {
            if (e[0] == 1) { if (alice.Union(e[1], e[2])) used++; }
            else if (e[0] == 2) { if (bob.Union(e[1], e[2])) used++; }
        }
        return alice.Components == 1 && bob.Components == 1 ? edges.Length - used : -1;
    }
}
