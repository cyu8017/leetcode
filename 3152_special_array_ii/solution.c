// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

#include <stdbool.h>
#include <stdlib.h>

bool* isArraySpecial(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* d = malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) d[i] = i;
    for (int i = 1; i < numsSize; i++)
        if (nums[i] % 2 != nums[i - 1] % 2) d[i] = d[i - 1];
    bool* ans = malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++)
        ans[i] = d[queries[i][1]] <= queries[i][0];
    free(d);
    *returnSize = queriesSize;
    return ans;
}
