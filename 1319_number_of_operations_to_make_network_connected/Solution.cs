// LeetCode 1319 - Number Of Operations To Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

public class Solution {
    public int MakeConnected(int n, int[][] connections) {
        if (connections.Length < n - 1) return -1;
        var parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            while (x != parent[x]) { parent[x] = parent[parent[x]]; x = parent[x]; }
            return x;
        }
        foreach (var e in connections) {
            int ra = Find(e[0]), rb = Find(e[1]);
            if (ra != rb) parent[ra] = rb;
        }
        var comps = new System.Collections.Generic.HashSet<int>();
        for (int i = 0; i < n; i++) comps.Add(Find(i));
        return comps.Count - 1;
    }
}
