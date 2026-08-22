// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

#include <stdlib.h>

long long maxPalindromicSubarraySum(int* nums, int numsSize) {
    int n = numsSize;
    long long* prefix = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    int* odd = (int*)malloc((size_t)n * sizeof(int));
    int left = 0, right = -1;
    for (int i = 0; i < n; i++) {
        int radius = 1;
        if (i <= right) {
            int mirror = left + right - i;
            radius = odd[mirror];
            if (right - i + 1 < radius) radius = right - i + 1;
        }
        while (i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]) radius++;
        odd[i] = radius;
        if (i + radius - 1 > right) {
            left = i - radius + 1;
            right = i + radius - 1;
        }
    }

    int* even = (int*)malloc((size_t)n * sizeof(int));
    left = 0;
    right = -1;
    for (int i = 0; i < n; i++) {
        int radius = 0;
        if (i <= right) {
            int mirror = left + right - i + 1;
            radius = even[mirror];
            if (right - i + 1 < radius) radius = right - i + 1;
        }
        while (i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]) radius++;
        even[i] = radius;
        if (i + radius - 1 > right) {
            left = i - radius;
            right = i + radius - 1;
        }
    }

    long long answer = 0;
    for (int i = 0; i < n; i++) {
        long long sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1];
        if (sum > answer) answer = sum;
        if (even[i] > 0) {
            sum = prefix[i + even[i]] - prefix[i - even[i]];
            if (sum > answer) answer = sum;
        }
    }

    free(prefix);
    free(odd);
    free(even);
    return answer;
}
