// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

#include <stdlib.h>

int* prisonAfterNDays(int* cells, int cellsSize, int n, int* returnSize) {
    (void)cellsSize;
    int seen[256];
    for (int i = 0; i < 256; i++) seen[i] = -1;
    int state = 0;
    for (int i = 0; i < 8; i++) state |= cells[i] << i;
    while (n) {
        if (seen[state] != -1) {
            int cycle = seen[state] - n;
            if (cycle > 0) n %= cycle;
            if (n == 0) break;
        }
        seen[state] = n;
        int nxt = 0;
        for (int i = 1; i <= 6; i++) {
            int left = (state >> (i - 1)) & 1;
            int right = (state >> (i + 1)) & 1;
            if (left == right) nxt |= 1 << i;
        }
        state = nxt;
        n--;
    }
    int* ans = (int*)calloc(8, sizeof(int));
    for (int i = 0; i < 8; i++) ans[i] = (state >> i) & 1;
    *returnSize = 8;
    return ans;
}
