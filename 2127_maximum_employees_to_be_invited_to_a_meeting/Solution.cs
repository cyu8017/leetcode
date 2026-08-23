// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

public class Solution {
    public int MaximumInvitations(int[] favorite) {
        int n = favorite.Length;
        int[] indeg = new int[n], depth = new int[n];
        Array.Fill(depth, 1);
        foreach (int f in favorite) indeg[f]++;
        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);
        while (q.Count > 0) {
            int u = q.Dequeue();
            int v = favorite[u];
            depth[v] = Math.Max(depth[v], depth[u] + 1);
            if (--indeg[v] == 0) q.Enqueue(v);
        }
        int pairSum = 0, maxCycle = 0;
        bool[] vis = new bool[n];
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0 || vis[i]) continue;
            int u = i, lenCycle = 0;
            while (!vis[u]) {
                vis[u] = true;
                u = favorite[u];
                lenCycle++;
            }
            if (lenCycle == 2) pairSum += depth[i] + depth[favorite[i]];
            else maxCycle = Math.Max(maxCycle, lenCycle);
        }
        return Math.Max(pairSum, maxCycle);
    }
}
