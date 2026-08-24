// CONFIG class=Solution method=finishTime types=None
// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] baseTime;

    public long finishTime(int n, int[][] edges, int[] baseTime) {
        this.baseTime = baseTime;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) g[e[0]].add(e[1]);
        return dfs(0);
    }

    private long dfs(int i) {
        if (g[i].isEmpty()) return baseTime[i];
        final long INF = 1L << 62;
        long earliest = INF, latest = -INF;
        for (int j : g[i]) {
            long a = dfs(j);
            earliest = Math.min(earliest, a);
            latest = Math.max(latest, a);
        }
        long ownDuration = (latest - earliest) + baseTime[i];
        return latest + ownDuration;
    }
}
