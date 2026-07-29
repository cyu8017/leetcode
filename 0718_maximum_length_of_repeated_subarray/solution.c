// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

#include <stdlib.h>
#include <string.h>

int findLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* dp = (int*)calloc((size_t)(nums2Size + 1), sizeof(int));
    int best = 0;
    for (int i = 1; i <= nums1Size; i++) {
        int* next = (int*)calloc((size_t)(nums2Size + 1), sizeof(int));
        for (int j = 1; j <= nums2Size; j++) {
            if (nums1[i - 1] == nums2[j - 1]) {
                next[j] = dp[j - 1] + 1;
                if (next[j] > best) {
                    best = next[j];
                }
            }
        }
        free(dp);
        dp = next;
    }
    free(dp);
    return best;
}
