// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

#include <stdlib.h>
#include <stdbool.h>
bool partitionArray(int* nums, int numsSize, int k) {
    if (numsSize % k != 0) return false;
    int m = numsSize / k, mx = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int* cnt = (int*)calloc((size_t)mx + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        if (++cnt[nums[i]] > m) { free(cnt); return false; }
    }
    free(cnt);
    return true;
}
