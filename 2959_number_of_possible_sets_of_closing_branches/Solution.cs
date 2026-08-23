// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

public class Solution {
    public int NumberOfSets(int n, int maxDistance, int[][] roads) {
        int ans = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int[][] dist = new int[n][];
            for (int i = 0; i < n; i++) {
                dist[i] = new int[n];
                for (int j = 0; j < n; j++) dist[i][j] = 1 << 29;
                dist[i][i] = 0;
            }
            foreach (var r in roads) {
                int u = r[0], v = r[1], w = r[2];
                if ((mask & (1 << u)) != 0 && (mask & (1 << v)) != 0) {
                    if (w < dist[u][v]) {
                        dist[u][v] = w;
                        dist[v][u] = w;
                    }
                }
            }
            for (int k = 0; k < n; k++) {
                if ((mask & (1 << k)) == 0) continue;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) == 0) continue;
                    for (int j = 0; j < n; j++) {
                        if ((mask & (1 << j)) == 0) continue;
                        if (dist[i][k] + dist[k][j] < dist[i][j])
                            dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
            bool ok = true;
            for (int i = 0; i < n && ok; i++) {
                if ((mask & (1 << i)) == 0) continue;
                for (int j = 0; j < n; j++) {
                    if ((mask & (1 << j)) == 0) continue;
                    if (dist[i][j] > maxDistance) { ok = false; break; }
                }
            }
            if (ok) ans++;
        }
        return ans;
    }
}
