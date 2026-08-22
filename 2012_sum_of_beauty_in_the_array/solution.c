// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

#include <stdlib.h>

int sumOfBeauties(int* nums, int numsSize) {
    int n = numsSize;
    int* prefixMax = (int*)malloc((size_t)n * sizeof(int));
    int* suffixMin = (int*)malloc((size_t)n * sizeof(int));
    prefixMax[0] = nums[0];
    for (int i = 1; i < n; i++) {
        prefixMax[i] = prefixMax[i - 1] > nums[i] ? prefixMax[i - 1] : nums[i];
    }
    suffixMin[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        suffixMin[i] = suffixMin[i + 1] < nums[i] ? suffixMin[i + 1] : nums[i];
    }
    int ans = 0;
    for (int i = 1; i < n - 1; i++) {
        if (prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1]) ans += 2;
        else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) ans++;
    }
    free(prefixMax); free(suffixMin);
    return ans;
}
