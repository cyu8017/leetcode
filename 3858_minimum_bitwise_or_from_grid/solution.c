// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

#include <stdbool.h>

static int bit_len(unsigned x) {
    int n = 0; while (x) { n++; x >>= 1; } return n;
}

int minimumOR(int** grid, int gridSize, int* gridColSize) {
    int mx = 0;
    for (int i = 0; i < gridSize; i++)
        for (int j = 0; j < gridColSize[i]; j++)
            if (grid[i][j] > mx) mx = grid[i][j];
    int m = bit_len((unsigned)mx);
    int ans = 0;
    for (int i = m - 1; i >= 0; i--) {
        int mask = ans | ((1 << i) - 1);
        for (int r = 0; r < gridSize; r++) {
            bool found = false;
            for (int j = 0; j < gridColSize[r]; j++) {
                if ((grid[r][j] | mask) == mask) { found = true; break; }
            }
            if (!found) { ans |= 1 << i; break; }
        }
    }
    return ans;
}
