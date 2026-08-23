// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

using System;
using System.Collections.Generic;

public class DistanceLimitedPathsExist {
    private readonly List<int> weights = new();
    private readonly List<int[]> versions = new();

    public DistanceLimitedPathsExist(int n, int[][] edgeList) {
        var edges = new List<int[]>();
        foreach (int[] edge in edgeList) {
            edges.Add(new[] { edge[2], edge[0], edge[1] });
        }
        edges.Sort((a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            if (a[1] != b[1]) return a[1].CompareTo(b[1]);
            return a[2].CompareTo(b[2]);
        });
        int[] parent = new int[n];
        int[] size = new int[n];
        for (int j = 0; j < n; j++) {
            parent[j] = j;
            size[j] = 1;
        }
        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        int i = 0;
        while (i < edges.Count) {
            int weight = edges[i][0];
            while (i < edges.Count && edges[i][0] == weight) {
                int ra = Find(edges[i][1]);
                int rb = Find(edges[i][2]);
                if (ra != rb) {
                    if (size[ra] < size[rb]) {
                        (ra, rb) = (rb, ra);
                    }
                    parent[rb] = ra;
                    size[ra] += size[rb];
                }
                i++;
            }
            weights.Add(weight);
            versions.Add((int[])parent.Clone());
        }
    }

    public bool Query(int p, int q, int limit) {
        int lo = 0;
        int hi = weights.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (weights[mid] < limit) lo = mid + 1;
            else hi = mid;
        }
        int idx = lo - 1;
        if (idx < 0) return p == q;
        int[] parent = versions[idx];
        int rp = p;
        while (parent[rp] != rp) rp = parent[rp];
        int rq = q;
        while (parent[rq] != rq) rq = parent[rq];
        return rp == rq;
    }
}
