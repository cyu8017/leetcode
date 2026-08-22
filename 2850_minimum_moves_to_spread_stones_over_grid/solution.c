// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

#include <stdlib.h>

static int iabs(int x) { return x < 0 ? -x : x; }

static int best2850;
static int zeros2850[9][2], zc2850;
static int extras2850[9][2], ec2850;
static int used2850[9];

static void dfs2850(int i, int cost) {
    if (cost >= best2850) return;
    if (i == zc2850) { best2850 = cost; return; }
    for (int j = 0; j < ec2850; j++) {
        if (used2850[j]) continue;
        used2850[j] = 1;
        int d = iabs(extras2850[j][0] - zeros2850[i][0]) + iabs(extras2850[j][1] - zeros2850[i][1]);
        dfs2850(i + 1, cost + d);
        used2850[j] = 0;
    }
}

int minimumMoves(int** grid, int gridSize, int* gridColSize) {
    (void)gridSize; (void)gridColSize;
    zc2850 = ec2850 = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grid[i][j] == 0) {
                zeros2850[zc2850][0] = i; zeros2850[zc2850][1] = j; zc2850++;
            } else if (grid[i][j] > 1) {
                for (int k = 0; k < grid[i][j] - 1; k++) {
                    extras2850[ec2850][0] = i; extras2850[ec2850][1] = j; ec2850++;
                }
            }
        }
    }
    if (zc2850 == 0) return 0;
    best2850 = 1 << 30;
    for (int i = 0; i < 9; i++) used2850[i] = 0;
    dfs2850(0, 0);
    return best2850;
}
