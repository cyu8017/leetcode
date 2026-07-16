// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

#include <stdlib.h>

static int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int absInt(int x) {
    return x < 0 ? -x : x;
}

int threeSumClosest(int* nums, int numsSize, int target) {
    qsort(nums, numsSize, sizeof(int), cmp);
    int closest = nums[0] + nums[1] + nums[2];

    for (int i = 0; i < numsSize - 2; i++) {
        int left = i + 1;
        int right = numsSize - 1;
        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];
            if (absInt(total - target) < absInt(closest - target)) {
                closest = total;
            }
            if (total < target) {
                left++;
            } else if (total > target) {
                right--;
            } else {
                return total;
            }
        }
    }

    return closest;
}
