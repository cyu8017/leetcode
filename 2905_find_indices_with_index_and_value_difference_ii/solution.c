// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

#include <stdlib.h>

int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    int* ans = (int*)malloc(2 * sizeof(int));
    int minIdx = 0, maxIdx = 0;
    for (int j = indexDifference; j < numsSize; j++) {
        int i = j - indexDifference;
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
        if (nums[j] - nums[minIdx] >= valueDifference) { ans[0] = minIdx; ans[1] = j; *returnSize = 2; return ans; }
        if (nums[maxIdx] - nums[j] >= valueDifference) { ans[0] = maxIdx; ans[1] = j; *returnSize = 2; return ans; }
    }
    ans[0] = -1; ans[1] = -1; *returnSize = 2; return ans;
}
