// LeetCode 3526 - Range XOR Queries With Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getResults(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* a = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a[i] = nums[i];
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int ac = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int typ = queries[qi][0];
        if (typ == 1) {
            int l = queries[qi][1], r = queries[qi][2];
            while (l < r) { int t = a[l]; a[l] = a[r]; a[r] = t; l++; r--; }
        } else if (typ == 2) {
            int l = queries[qi][1], r = queries[qi][2], x = 0;
            for (int i = l; i <= r; i++) x ^= a[i];
            ans[ac++] = x;
        } else {
            a[queries[qi][1]] = queries[qi][2];
        }
    }
    free(a);
    *returnSize = ac;
    return ans;
}
