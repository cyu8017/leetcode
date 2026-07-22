// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

#include <stdlib.h>
#include <string.h>

int maximumUniqueSubarray(int* nums, int numsSize) {
    int* last = (int*)malloc(10001 * sizeof(int));
    for (int i = 0; i < 10001; i++) last[i] = -1;
    int left = 0, cur = 0, best = 0;
    for (int right = 0; right < numsSize; right++) {
        int x = nums[right];
        if (last[x] >= left) {
            int stop = last[x];
            while (left <= stop) cur -= nums[left++];
        }
        last[x] = right;
        cur += x;
        if (cur > best) best = cur;
    }
    free(last);
    return best;
}
