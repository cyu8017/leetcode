// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

#include <stdlib.h>
#include <string.h>

int* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int m = numsSize - k + 1;
    int* ans = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        int vals[64], freq[64], fn = 0;
        for (int j = i; j < i + k; j++) {
            int found = -1;
            for (int t = 0; t < fn; t++) if (vals[t] == nums[j]) { found = t; break; }
            if (found < 0) {
                if (fn < 64) { vals[fn] = nums[j]; freq[fn] = 1; fn++; }
            } else freq[found]++;
        }
        /* sort by freq desc, value desc */
        for (int a = 0; a < fn; a++)
            for (int b = a + 1; b < fn; b++)
                if (freq[b] > freq[a] || (freq[b] == freq[a] && vals[b] > vals[a])) {
                    int tv = vals[a], tf = freq[a];
                    vals[a] = vals[b]; freq[a] = freq[b];
                    vals[b] = tv; freq[b] = tf;
                }
        int lim = x < fn ? x : fn;
        int keep[64]; memset(keep, 0, sizeof(keep));
        /* mark keep by value - use parallel */
        int keepV[64];
        for (int t = 0; t < lim; t++) keepV[t] = vals[t];
        int sum = 0;
        for (int j = i; j < i + k; j++) {
            for (int t = 0; t < lim; t++) if (nums[j] == keepV[t]) { sum += nums[j]; break; }
        }
        ans[i] = sum;
    }
    *returnSize = m;
    return ans;
}
