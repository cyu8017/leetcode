// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

#include <stdlib.h>

long long continuousSubarrays(int* nums, int numsSize) {
    long long ans = 0;
    int left = 0;
    // value range can be large; use sliding window with min/max deques
    int* minq = (int*)malloc(numsSize * sizeof(int));
    int* maxq = (int*)malloc(numsSize * sizeof(int));
    int minh = 0, mint = 0, maxh = 0, maxt = 0;
    for (int right = 0; right < numsSize; right++) {
        while (mint > minh && nums[minq[mint - 1]] >= nums[right]) mint--;
        minq[mint++] = right;
        while (maxt > maxh && nums[maxq[maxt - 1]] <= nums[right]) maxt--;
        maxq[maxt++] = right;
        while (nums[maxq[maxh]] - nums[minq[minh]] > 2) {
            left++;
            if (minq[minh] < left) minh++;
            if (maxq[maxh] < left) maxh++;
        }
        ans += right - left + 1;
    }
    free(minq); free(maxq);
    return ans;
}
