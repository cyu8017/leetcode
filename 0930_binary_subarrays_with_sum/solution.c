// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

#include <stdlib.h>

int numSubarraysWithSum(int* nums, int numsSize, int goal) {
    int* count = (int*)calloc((size_t)(numsSize + 1), sizeof(int));
    count[0] = 1;
    int prefix = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        if (prefix - goal >= 0) ans += count[prefix - goal];
        count[prefix]++;
    }
    free(count);
    return ans;
}
