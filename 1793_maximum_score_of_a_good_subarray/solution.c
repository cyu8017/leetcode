// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

#include <stdlib.h>

int maximumScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* stack = (int*)malloc((n + 1) * sizeof(int));
    int top = -1;
    long long ans = 0;
    for (int i = 0; i <= n; i++) {
        while (top >= 0 && (i == n || nums[i] < nums[stack[top]])) {
            int mid = stack[top--];
            int left = top >= 0 ? stack[top] + 1 : 0;
            int right = i - 1;
            if (left <= k && k <= right) {
                long long score = (long long)nums[mid] * (right - left + 1);
                if (score > ans) ans = score;
            }
        }
        stack[++top] = i;
    }
    free(stack);
    return (int)ans;
}
