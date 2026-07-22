// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

using System;
using System.Linq;

public class Solution {
    public bool[] DistanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        int[] parent = Enumerable.Range(0, n).ToArray();
        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        var ans = new bool[queries.Length];
        Array.Sort(edgeList, (a, b) => a[2].CompareTo(b[2]));
        var ordered = queries
            .Select((q, j) => (limit: q[2], p: q[0], q: q[1], idx: j))
            .OrderBy(t => t.limit)
            .ToArray();
        int i = 0;
        foreach (var (limit, p, q, idx) in ordered) {
            while (i < edgeList.Length && edgeList[i][2] < limit) {
                int a = edgeList[i][0], b = edgeList[i][1];
                parent[Find(a)] = Find(b);
                i++;
            }
            ans[idx] = Find(p) == Find(q);
        }
        return ans;
    }
}
