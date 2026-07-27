// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

#include <stdlib.h>

int validSubarrays(int* nums, int numsSize) {
    int* stack = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        while (top > 0 && nums[stack[top - 1]] > nums[i]) {
            int j = stack[--top];
            ans += i - j;
        }
        stack[top++] = i;
    }
    while (top > 0) {
        int j = stack[--top];
        ans += numsSize - j;
    }
    free(stack);
    return ans;
}
