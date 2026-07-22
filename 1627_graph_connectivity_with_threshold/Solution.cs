// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

using System.Collections.Generic;

public class Solution {
    public IList<bool> AreConnected(int n, int threshold, int[][] queries) {
        var parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        int Find(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        for (int d = threshold + 1; d <= n; d++) {
            for (int x = 2 * d; x <= n; x += d) {
                int a = Find(d), b = Find(x);
                if (a != b) parent[b] = a;
            }
        }
        var ans = new List<bool>(queries.Length);
        foreach (var q in queries) ans.Add(Find(q[0]) == Find(q[1]));
        return ans;
    }
}
