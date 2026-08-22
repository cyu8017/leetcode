// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

#include <stdlib.h>

static int cmp_row(const void* a, const void* b) {
    int* const* aa = (int* const*)a; int* const* bb = (int* const*)b;
    return (*aa)[0] - (*bb)[0];
}
static int cmp_col(const void* a, const void* b) {
    int* const* aa = (int* const*)a; int* const* bb = (int* const*)b;
    return (*aa)[1] - (*bb)[1];
}
static int abs3189(int x) { return x < 0 ? -x : x; }

int minMoves(int** rooks, int rooksSize, int* rooksColSize) {
    (void)rooksColSize;
    int ans = 0;
    qsort(rooks, rooksSize, sizeof(int*), cmp_row);
    for (int i = 0; i < rooksSize; i++) ans += abs3189(rooks[i][0] - i);
    qsort(rooks, rooksSize, sizeof(int*), cmp_col);
    for (int j = 0; j < rooksSize; j++) ans += abs3189(rooks[j][1] - j);
    return ans;
}
