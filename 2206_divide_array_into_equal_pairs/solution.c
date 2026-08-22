// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

#include <stdlib.h>
#include <stdbool.h>

bool divideArray(int* nums, int numsSize) {
    int maxv = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxv) maxv = nums[i];
    int* freq = (int*)calloc((size_t)maxv + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) freq[nums[i]]++;
    for (int i = 0; i <= maxv; i++) if (freq[i] % 2) { free(freq); return false; }
    free(freq);
    return true;
}
