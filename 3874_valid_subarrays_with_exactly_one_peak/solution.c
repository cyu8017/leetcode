// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

#include <stdlib.h>

long long validSubarrays(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* peaks = (int*)malloc((size_t)n * sizeof(int));
    int psz = 0;
    for (int i = 1; i < n - 1; i++) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks[psz++] = i;
    }
    long long ans = 0;
    for (int j = 0; j < psz; j++) {
        int p = peaks[j];
        int leftMin = p - k; if (leftMin < 0) leftMin = 0;
        if (j > 0) {
            int v = peaks[j - 1] + 1;
            if (v > leftMin) leftMin = v;
        }
        int rightMax = p + k; if (rightMax > n - 1) rightMax = n - 1;
        if (j < psz - 1) {
            int v = peaks[j + 1] - 1;
            if (v < rightMax) rightMax = v;
        }
        ans += (long long)(p - leftMin + 1) * (rightMax - p + 1);
    }
    free(peaks);
    return ans;
}
