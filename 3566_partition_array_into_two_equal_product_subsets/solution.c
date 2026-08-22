// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

#include <stdbool.h>

bool checkEqualPartitions(int* nums, int numsSize, long long target) {
    int n = numsSize;
    for (int i = 0; i < (1 << n); i++) {
        long long x = 1, y = 1;
        for (int j = 0; j < n; j++) {
            if ((i >> j) & 1) x *= nums[j];
            else y *= nums[j];
            if (x > target || y > target) break;
        }
        if (x == target && y == target) return true;
    }
    return false;
}
