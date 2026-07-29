// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

#include <stdlib.h>
#include <string.h>

static int canCross(int day, int row, int col, int** cells) {
    int* blocked = (int*)calloc((size_t)row * col, sizeof(int));
    for (int i = 0; i < day; i++) {
        int r = cells[i][0] - 1, c = cells[i][1] - 1;
        blocked[r * col + c] = 1;
    }
    int* stackR = (int*)malloc((size_t)row * col * sizeof(int));
    int* stackC = (int*)malloc((size_t)row * col * sizeof(int));
    int* seen = (int*)calloc((size_t)row * col, sizeof(int));
    int top = 0;
    for (int c = 0; c < col; c++) {
        if (!blocked[c]) {
            stackR[top] = 0;
            stackC[top] = c;
            seen[c] = 1;
            top++;
        }
    }
    int ok = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (top) {
        int r = stackR[--top], c = stackC[top];
        if (r == row - 1) { ok = 1; break; }
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nc < 0 || nr >= row || nc >= col) continue;
            int id = nr * col + nc;
            if (blocked[id] || seen[id]) continue;
            seen[id] = 1;
            stackR[top] = nr;
            stackC[top] = nc;
            top++;
        }
    }
    free(blocked); free(stackR); free(stackC); free(seen);
    return ok;
}

int latestDayToCross(int row, int col, int** cells, int cellsSize, int* cellsColSize) {
    (void)cellsColSize;
    int lo = 1, hi = cellsSize, ans = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (canCross(mid, row, col, cells)) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return ans;
}
