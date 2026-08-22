// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

#include <stdlib.h>
#include <string.h>

int countRoutes(char** grid, int gridSize, int d) {
    const int mod = 1000000007;
    int n = gridSize;
    int m = (int)strlen(grid[0]);
    int upRadius = 0;
    while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
    int* arrived = (int*)calloc((size_t)m, sizeof(int));
    for (int c = 0; c < m; c++) if (grid[n - 1][c] == '.') arrived[c] = 1;
    for (int r = n - 1; r >= 0; r--) {
        int* pref = (int*)calloc((size_t)m + 1, sizeof(int));
        for (int i = 0; i < m; i++) pref[i + 1] = (pref[i] + arrived[i]) % mod;
        int* horizontal = (int*)calloc((size_t)m, sizeof(int));
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == '#') continue;
            int l = c - d, rr = c + d;
            if (l < 0) l = 0;
            if (rr >= m) rr = m - 1;
            int h = (pref[rr + 1] - pref[l] - arrived[c]) % mod;
            if (h < 0) h += mod;
            horizontal[c] = h;
        }
        if (r == 0) {
            int ans = 0;
            for (int c = 0; c < m; c++) ans = (ans + arrived[c] + horizontal[c]) % mod;
            free(pref); free(horizontal); free(arrived);
            return ans;
        }
        int* pref2 = (int*)calloc((size_t)m + 1, sizeof(int));
        for (int c = 0; c < m; c++) pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % mod;
        int* next = (int*)calloc((size_t)m, sizeof(int));
        for (int c = 0; c < m; c++) {
            if (grid[r - 1][c] == '#') continue;
            int l = c - upRadius, rr = c + upRadius;
            if (l < 0) l = 0;
            if (rr >= m) rr = m - 1;
            int v = pref2[rr + 1] - pref2[l];
            if (v < 0) v += mod;
            next[c] = v;
        }
        free(pref); free(horizontal); free(pref2); free(arrived);
        arrived = next;
    }
    free(arrived);
    return 0;
}
