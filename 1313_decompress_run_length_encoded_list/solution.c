// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

#include <stdlib.h>

int* decompressRLElist(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i += 2) total += nums[i];
    int* ans = (int*)malloc(total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < numsSize; i += 2)
        for (int j = 0; j < nums[i]; j++) ans[idx++] = nums[i + 1];
    *returnSize = total;
    return ans;
}
