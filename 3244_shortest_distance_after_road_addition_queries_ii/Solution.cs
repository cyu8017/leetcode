// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

using System.Collections.Generic;

public class Solution {
    public int[] ShortestDistanceAfterQueries(int n, int[][] queries) {
        int[] nxt = new int[n - 1];
        for (int i = 0; i < n - 1; i++) nxt[i] = i + 1;
        int cnt = n - 1;
        var ans = new List<int>();
        foreach (var q in queries) {
            int u = q[0], v = q[1];
            if (nxt[u] > 0 && nxt[u] < v) {
                int i = nxt[u];
                while (i < v) {
                    cnt--;
                    int ni = nxt[i];
                    nxt[i] = 0;
                    i = ni;
                }
                nxt[u] = v;
            }
            ans.Add(cnt);
        }
        return ans.ToArray();
    }
}
