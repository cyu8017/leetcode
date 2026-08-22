// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

#include <stdlib.h>
#include <stdbool.h>

static int cmp2708(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxStrength(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp2708);
    if (numsSize == 1) return nums[0];
    long long prod = 1;
    bool used = false;
    int i = 0;
    while (i + 1 < numsSize && nums[i] < 0 && nums[i + 1] < 0) {
        prod *= (long long)nums[i] * nums[i + 1];
        used = true;
        i += 2;
    }
    bool negLeft = i < numsSize && nums[i] < 0;
    for (; i < numsSize; i++) {
        if (nums[i] > 0) { prod *= nums[i]; used = true; }
    }
    if (!used) {
        if (negLeft) {
            for (int j = 0; j < numsSize; j++) if (nums[j] == 0) return 0;
            return nums[numsSize - 1];
        }
        return 0;
    }
    return prod;
}
