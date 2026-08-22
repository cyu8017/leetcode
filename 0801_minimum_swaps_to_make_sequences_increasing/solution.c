// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

#include <stdlib.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int minSwap(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int* swap = (int*)malloc((size_t)n * sizeof(int));
    int* keep = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        swap[i] = n;
        keep[i] = n;
    }
    swap[0] = 1;
    keep[0] = 0;
    for (int i = 1; i < n; i++) {
        if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
            keep[i] = keep[i - 1];
            swap[i] = swap[i - 1] + 1;
        }
        if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
            keep[i] = MIN(keep[i], swap[i - 1]);
            swap[i] = MIN(swap[i], keep[i - 1] + 1);
        }
    }
    int ans = MIN(swap[n - 1], keep[n - 1]);
    free(swap);
    free(keep);
    return ans;
}
