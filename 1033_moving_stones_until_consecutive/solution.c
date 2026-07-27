// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

#include <stdlib.h>

static void sort3(int* a, int* b, int* c) {
    if (*a > *b) { int t = *a; *a = *b; *b = t; }
    if (*b > *c) { int t = *b; *b = *c; *c = t; }
    if (*a > *b) { int t = *a; *a = *b; *b = t; }
}

int* numMovesStones(int a, int b, int c, int* returnSize) {
    sort3(&a, &b, &c);
    int minMoves;
    if (c - a == 2) minMoves = 0;
    else if (b - a <= 2 || c - b <= 2) minMoves = 1;
    else minMoves = 2;
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = minMoves;
    ans[1] = c - a - 2;
    *returnSize = 2;
    return ans;
}
