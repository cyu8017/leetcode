// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

#include <stdbool.h>
#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

static bool dfs(int* nums, int n, int* buckets, int k, int target, int index) {
    if (index == n) return true;
    for (int i = 0; i < k; i++) {
        if (buckets[i] + nums[index] > target) continue;
        buckets[i] += nums[index];
        if (dfs(nums, n, buckets, k, target, index + 1)) return true;
        buckets[i] -= nums[index];
        if (buckets[i] == 0) break;
    }
    return false;
}

bool canPartitionKSubsets(int* nums, int numsSize, int k) {
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) sum += nums[i];
    if (sum % k) return false;
    int target = (int)(sum / k);
    qsort(nums, (size_t)numsSize, sizeof(int), cmpDesc);
    if (nums[0] > target) return false;
    int* buckets = (int*)calloc((size_t)k, sizeof(int));
    bool ok = dfs(nums, numsSize, buckets, k, target, 0);
    free(buckets);
    return ok;
}
