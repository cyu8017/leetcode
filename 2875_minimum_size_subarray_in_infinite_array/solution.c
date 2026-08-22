// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

#include <stdlib.h>

int minSizeSubarray(int* nums, int numsSize, int target) {
    int n = numsSize;
    long long total = 0;
    for (int i = 0; i < n; i++) total += nums[i];
    int ans = 1 << 30;
    if (total > 0) {
        int loops = (int)(target / total);
        int remain = (int)(target % total);
        if (remain == 0) return loops * n;
        int* arr = (int*)malloc(2 * n * sizeof(int));
        for (int i = 0; i < n; i++) { arr[i] = nums[i]; arr[n + i] = nums[i]; }
        int left = 0, sum = 0, best = 1 << 30;
        for (int right = 0; right < 2 * n; right++) {
            sum += arr[right];
            while (sum > remain && left <= right) { sum -= arr[left]; left++; }
            if (sum == remain && right - left + 1 < best) best = right - left + 1;
        }
        free(arr);
        if (best < (1 << 30)) ans = loops * n + best;
    }
    return ans == (1 << 30) ? -1 : ans;
}
