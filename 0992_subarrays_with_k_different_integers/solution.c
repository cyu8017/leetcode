// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

#include <stdlib.h>

static int atMost(int* nums, int numsSize, int m) {
    if (m < 0) return 0;
    int* count = (int*)calloc((size_t)(numsSize + 1), sizeof(int));
    int left = 0, ans = 0, kinds = 0;
    for (int right = 0; right < numsSize; right++) {
        if (count[nums[right]]++ == 0) kinds++;
        while (kinds > m) {
            if (--count[nums[left]] == 0) kinds--;
            left++;
        }
        ans += right - left + 1;
    }
    free(count);
    return ans;
}

int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    return atMost(nums, numsSize, k) - atMost(nums, numsSize, k - 1);
}
