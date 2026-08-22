// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool canPartition(int* nums, int numsSize) {
    int total = 0;
    for (int index = 0; index < numsSize; index++) {
        total += nums[index];
    }
    if (total % 2) {
        return false;
    }

    int target = total / 2;
    bool* possible = (bool*)calloc((size_t)target + 1, sizeof(bool));
    possible[0] = true;

    for (int index = 0; index < numsSize; index++) {
        int value = nums[index];
        for (int amount = target; amount >= value; amount--) {
            if (possible[amount - value]) {
                possible[amount] = true;
            }
        }
        if (possible[target]) {
            free(possible);
            return true;
        }
    }

    bool result = possible[target];
    free(possible);
    return result;
}
