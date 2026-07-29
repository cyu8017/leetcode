// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

static bool find_sub(int* nums, int n, int target, int count, int index) {
    if (count == 0) return target == 0;
    if (index == n || count + index > n || target < 0) return false;
    return find_sub(nums, n, target - nums[index], count - 1, index + 1) ||
           find_sub(nums, n, target, count, index + 1);
}

bool splitArraySameAverage(int* nums, int numsSize) {
    int n = numsSize, total = 0;
    for (int i = 0; i < n; i++) total += nums[i];
    qsort(nums, (size_t)n, sizeof(int), cmp_int);
    for (int size = 1; size < n; size++) {
        if ((total * size) % n == 0 && find_sub(nums, n, total * size / n, size, 0))
            return true;
    }
    return false;
}
