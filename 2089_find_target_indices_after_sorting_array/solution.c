// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

#include <stdlib.h>

int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int less = 0, eq = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < target) less++;
        else if (nums[i] == target) eq++;
    }
    int* ans = (int*)malloc((size_t)(eq ? eq : 1) * sizeof(int));
    for (int i = 0; i < eq; i++) ans[i] = less + i;
    *returnSize = eq;
    return ans;
}
