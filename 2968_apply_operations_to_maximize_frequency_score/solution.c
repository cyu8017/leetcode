// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

#include <stdlib.h>

static int cmp2968(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxFrequencyScore(int* nums, int numsSize, long long k) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) arr[i] = nums[i];
    qsort(arr, (size_t)numsSize, sizeof(int), cmp2968);
    long long* pref = (long long*)malloc((size_t)(numsSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < numsSize; i++) pref[i + 1] = pref[i] + arr[i];
    int ans = 1;
    int left = 0;
    for (int right = 0; right < numsSize; right++) {
        while (1) {
            int mid = (left + right) / 2;
            long long leftCost = (long long)arr[mid] * (mid - left) - (pref[mid] - pref[left]);
            long long rightCost = (pref[right + 1] - pref[mid + 1]) - (long long)arr[mid] * (right - mid);
            if (leftCost + rightCost <= k) break;
            left++;
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    free(arr);
    free(pref);
    return ans;
}
