// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* relocateMarbles(int* nums, int numsSize, int* moveFrom, int moveFromSize, int* moveTo, int moveToSize, int* returnSize) {
    (void)moveToSize;
    // Use sorted unique set via array; positions up to 1e9 so use hash via open addressing on keys present
    int cap = numsSize + moveFromSize + 8;
    int* keys = (int*)malloc(cap * sizeof(int));
    bool* alive = (bool*)calloc(cap, sizeof(bool));
    int sz = 0;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i], found = -1;
        for (int j = 0; j < sz; j++) if (keys[j] == v) { found = j; break; }
        if (found < 0) { keys[sz] = v; alive[sz] = true; sz++; }
        else alive[found] = true;
    }
    for (int i = 0; i < moveFromSize; i++) {
        int from = moveFrom[i], to = moveTo[i];
        for (int j = 0; j < sz; j++) if (keys[j] == from) alive[j] = false;
        int found = -1;
        for (int j = 0; j < sz; j++) if (keys[j] == to) { found = j; break; }
        if (found < 0) { keys[sz] = to; alive[sz] = true; sz++; }
        else alive[found] = true;
    }
    int* ans = (int*)malloc(sz * sizeof(int));
    int out = 0;
    for (int i = 0; i < sz; i++) if (alive[i]) ans[out++] = keys[i];
    qsort(ans, out, sizeof(int), cmp_int);
    free(keys); free(alive);
    *returnSize = out;
    return ans;
}
