// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

#include <string.h>

int sumOfUnique(int* nums, int numsSize) {
    int counts[101];
    memset(counts, 0, sizeof(counts));
    for (int i = 0; i < numsSize; i++) {
        counts[nums[i]]++;
    }
    int total = 0;
    for (int value = 1; value <= 100; value++) {
        if (counts[value] == 1) {
            total += value;
        }
    }
    return total;
}
