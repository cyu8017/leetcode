// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

import java.util.*;

class DSU {
    int[] parent;
    int components;

    DSU(int n) {
        parent = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }
        components = n;
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            return false;
        }
        parent[a] = b;
        components--;
        return true;
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        DSU alice = new DSU(n);
        DSU bob = new DSU(n);
        int used = 0;
        for (int[] edge : edges) {
            if (edge[0] == 3) {
                boolean merged = alice.union(edge[1], edge[2]);
                bob.union(edge[1], edge[2]);
                if (merged) {
                    used++;
                }
            }
        }
        for (int[] edge : edges) {
            if (edge[0] == 1) {
                if (alice.union(edge[1], edge[2])) {
                    used++;
                }
            } else if (edge[0] == 2) {
                if (bob.union(edge[1], edge[2])) {
                    used++;
                }
            }
        }
        return alice.components == 1 && bob.components == 1 ? edges.length - used : -1;
    }
}
