// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

#include <stdlib.h>
#include <string.h>

int* arrayChange(int* nums, int numsSize, int** operations, int operationsSize, int* operationsColSize, int* returnSize) {
    (void)operationsColSize;
    int maxv = 1000001;
    int* pos = (int*)malloc((size_t)maxv * sizeof(int));
    memset(pos, -1, (size_t)maxv * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        pos[nums[i]] = i;
    }
    for (int i = 0; i < operationsSize; i++) {
        int from = operations[i][0];
        int to = operations[i][1];
        int idx = pos[from];
        nums[idx] = to;
        pos[from] = -1;
        pos[to] = idx;
    }
    free(pos);
    *returnSize = numsSize;
    return nums;
}
