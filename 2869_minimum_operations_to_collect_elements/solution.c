// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minOperations(int* nums, int numsSize, int k) {
    bool* need = (bool*)calloc(k + 1, sizeof(bool));
    int remain = k;
    for (int i = 1; i <= k; i++) need[i] = true;
    for (int i = numsSize - 1; i >= 0; i--) {
        if (nums[i] <= k && need[nums[i]]) {
            need[nums[i]] = false;
            remain--;
        }
        if (remain == 0) { free(need); return numsSize - i; }
    }
    free(need);
    return numsSize;
}
