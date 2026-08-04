// LeetCode 1489 - Find Critical And Pseudo Critical Edges In Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

import java.util.*;

class Solution {
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        int m = edges.length;
        int[][] es = new int[m][4];
        for (int i = 0; i < m; i++) {
            es[i][0] = edges[i][2];
            es[i][1] = edges[i][0];
            es[i][2] = edges[i][1];
            es[i][3] = i;
        }
        Arrays.sort(es, Comparator.comparingInt(a -> a[0]));
        int base = mst(n, es, -1, -1);
        List<Integer> critical = new ArrayList<>(), pseudo = new ArrayList<>();
        for (int j = 0; j < m; j++) {
            if (mst(n, es, j, -1) > base) critical.add(es[j][3]);
            else if (mst(n, es, -1, j) == base) pseudo.add(es[j][3]);
        }
        Collections.sort(critical);
        Collections.sort(pseudo);
        return List.of(critical, pseudo);
    }

    private int mst(int n, int[][] es, int skip, int force) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int total = 0, used = 0;
        if (force >= 0) {
            int[] e = es[force];
            parent[find(parent, e[1])] = find(parent, e[2]);
            total += e[0];
            used++;
        }
        for (int j = 0; j < es.length; j++) {
            if (j == skip || j == force) continue;
            int[] e = es[j];
            int x = find(parent, e[1]), y = find(parent, e[2]);
            if (x != y) {
                parent[x] = y;
                total += e[0];
                used++;
            }
        }
        return used == n - 1 ? total : Integer.MAX_VALUE / 2;
    }

    private int find(int[] parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
}
