// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

#include <stdlib.h>
#include <string.h>

int countSubarrays(int* nums, int numsSize, int k) {
    int pos = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] == k) { pos = i; break; }
    /* balance in [-n, n] -> index + n */
    int off = numsSize;
    int* bal = (int*)calloc((size_t)(2 * numsSize + 5), sizeof(int));
    bal[off + 0] = 1;
    int cur = 0;
    for (int i = pos - 1; i >= 0; i--) {
        cur += (nums[i] < k) ? -1 : 1;
        bal[off + cur]++;
    }
    int ans = bal[off + 0] + bal[off + 1];
    cur = 0;
    for (int i = pos + 1; i < numsSize; i++) {
        cur += (nums[i] < k) ? -1 : 1;
        ans += bal[off - cur] + bal[off + (1 - cur)];
    }
    free(bal);
    return ans;
}
