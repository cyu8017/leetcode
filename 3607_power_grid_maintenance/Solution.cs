// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

using System.Collections.Generic;

public class Solution {
    public int[] ProcessQueries(int c, int[][] connections, int[][] queries) {
        int[] parent = new int[c + 1];
        for (int i = 0; i <= c; i++) parent[i] = i;
        int Find(int x) => parent[x] == x ? x : parent[x] = Find(parent[x]);
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) {
                if (ra < rb) parent[rb] = ra;
                else parent[ra] = rb;
            }
        }
        foreach (var e in connections) Unite(e[0], e[1]);
        bool[] online = new bool[c + 1];
        for (int i = 0; i <= c; i++) online[i] = true;
        var comp = new Dictionary<int, List<int>>();
        for (int i = 1; i <= c; i++) {
            int r = Find(i);
            if (!comp.ContainsKey(r)) comp[r] = new List<int>();
            comp[r].Add(i);
        }
        foreach (var ids in comp.Values) ids.Sort();
        var ptr = new Dictionary<int, int>();
        var ans = new List<int>();
        foreach (var q in queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                online[x] = false;
                continue;
            }
            if (online[x]) {
                ans.Add(x);
                continue;
            }
            int r = Find(x);
            var ids = comp[r];
            if (!ptr.ContainsKey(r)) ptr[r] = 0;
            while (ptr[r] < ids.Count && !online[ids[ptr[r]]]) ptr[r]++;
            ans.Add(ptr[r] < ids.Count ? ids[ptr[r]] : -1);
        }
        return ans.ToArray();
    }
}
