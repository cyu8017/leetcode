// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

#include <vector>

class Solution {
public:
    int numberOfSets(int n, int maxDistance, std::vector<std::vector<int>>& roads) {
        int ans = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            std::vector<std::vector<int>> dist(n, std::vector<int>(n, 1 << 29));
            for (int i = 0; i < n; i++) dist[i][i] = 0;
            for (auto& r : roads) {
                int u = r[0], v = r[1], w = r[2];
                if ((mask & (1 << u)) && (mask & (1 << v))) {
                    if (w < dist[u][v]) {
                        dist[u][v] = w;
                        dist[v][u] = w;
                    }
                }
            }
            for (int k = 0; k < n; k++) {
                if (!(mask & (1 << k))) continue;
                for (int i = 0; i < n; i++) {
                    if (!(mask & (1 << i))) continue;
                    for (int j = 0; j < n; j++) {
                        if (!(mask & (1 << j))) continue;
                        if (dist[i][k] + dist[k][j] < dist[i][j])
                            dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
            bool ok = true;
            for (int i = 0; i < n && ok; i++) {
                if (!(mask & (1 << i))) continue;
                for (int j = 0; j < n; j++) {
                    if (!(mask & (1 << j))) continue;
                    if (dist[i][j] > maxDistance) { ok = false; break; }
                }
            }
            if (ok) ans++;
        }
        return ans;
    }
};
