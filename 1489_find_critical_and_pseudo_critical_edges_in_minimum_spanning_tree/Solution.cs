// LeetCode 1489 - Find Critical And Pseudo Critical Edges In Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<IList<int>> FindCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        var es = edges.Select((e, i) => (w: e[2], a: e[0], b: e[1], i)).OrderBy(t => t.w).ToArray();
        long Mst(int skip = -1, int force = -1) {
            var parent = Enumerable.Range(0, n).ToArray();
            int Find(int x) { while (x != parent[x]) { parent[x] = parent[parent[x]]; x = parent[x]; } return x; }
            long total = 0; int used = 0;
            if (force >= 0) {
                var e = es[force]; parent[Find(e.a)] = Find(e.b); total += e.w; used++;
            }
            for (int j = 0; j < es.Length; j++) {
                if (j == skip || j == force) continue;
                var e = es[j]; int x = Find(e.a), y = Find(e.b);
                if (x != y) { parent[x] = y; total += e.w; used++; }
            }
            return used == n - 1 ? total : long.MaxValue / 4;
        }
        long bas = Mst();
        var critical = new List<int>(); var pseudo = new List<int>();
        for (int j = 0; j < es.Length; j++) {
            if (Mst(skip: j) > bas) critical.Add(es[j].i);
            else if (Mst(force: j) == bas) pseudo.Add(es[j].i);
        }
        critical.Sort(); pseudo.Sort();
        return new List<IList<int>> { critical, pseudo };
    }
}
