// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool isPossibleDivide(int* nums, int numsSize, int k) {
    if (numsSize % k) return false;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int* counts = (int*)calloc(100001, sizeof(int));
    for (int i = 0; i < numsSize; i++) counts[nums[i]]++;
    for (int i = 0; i < numsSize; i++) {
        int start = nums[i];
        if (!counts[start]) continue;
        int amount = counts[start];
        for (int value = start; value < start + k; value++) {
            if (counts[value] < amount) {
                free(counts);
                return false;
            }
            counts[value] -= amount;
        }
    }
    free(counts);
    return true;
}
