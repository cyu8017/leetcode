// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

#include <stdbool.h>
#include <string.h>

int countLatticePoints(int** circles, int circlesSize, int* circlesColSize) {
    (void)circlesColSize;
    // coords can be in [-50, 250]; offset by 50 -> [0, 300]
    enum { OFF = 50, N = 301 };
    bool seen[N][N];
    memset(seen, 0, sizeof(seen));
    int ans = 0;
    for (int c = 0; c < circlesSize; c++) {
        int x = circles[c][0], y = circles[c][1], r = circles[c][2];
        for (int i = x - r; i <= x + r; i++) {
            for (int j = y - r; j <= y + r; j++) {
                if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r) {
                    int ii = i + OFF, jj = j + OFF;
                    if (!seen[ii][jj]) {
                        seen[ii][jj] = true;
                        ans++;
                    }
                }
            }
        }
    }
    return ans;
}
