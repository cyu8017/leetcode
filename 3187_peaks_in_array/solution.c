// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

#include <stdlib.h>

typedef struct { int n; int* c; } BIT3187;
static void bit_upd(BIT3187* b, int x, int d) { for (; x <= b->n; x += x & -x) b->c[x] += d; }
static int bit_qry(BIT3187* b, int x) { int s = 0; for (; x > 0; x -= x & -x) s += b->c[x]; return s; }

int* countOfPeaks(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = numsSize;
    BIT3187 tree = {n - 1, calloc(n, sizeof(int))};
    #define UPDATE(i, val) do { \
        int _i = (i); \
        if (_i > 0 && _i < n - 1 && nums[_i - 1] < nums[_i] && nums[_i] > nums[_i + 1]) \
            bit_upd(&tree, _i, (val)); \
    } while (0)
    for (int i = 1; i < n - 1; i++) UPDATE(i, 1);
    int* ans = malloc(queriesSize * sizeof(int));
    int an = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        if (queries[qi][0] == 1) {
            int l = queries[qi][1] + 1, r = queries[qi][2] - 1, t = 0;
            if (l <= r) t = bit_qry(&tree, r) - bit_qry(&tree, l - 1);
            ans[an++] = t;
        } else {
            int idx = queries[qi][1], val = queries[qi][2];
            for (int i = idx - 1; i <= idx + 1; i++) UPDATE(i, -1);
            nums[idx] = val;
            for (int i = idx - 1; i <= idx + 1; i++) UPDATE(i, 1);
        }
    }
    #undef UPDATE
    free(tree.c);
    *returnSize = an;
    return ans;
}
