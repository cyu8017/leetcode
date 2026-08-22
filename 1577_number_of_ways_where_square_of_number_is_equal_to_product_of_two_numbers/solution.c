// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

#include <stdlib.h>

static int countTriplets(int* a, int aSize, int* b, int bSize) {
    int ans = 0;
    for (int i = 0; i < aSize; i++) {
        long long sq = (long long)a[i] * a[i];
        for (int j = 0; j < bSize; j++) {
            for (int k = j + 1; k < bSize; k++) {
                if ((long long)b[j] * b[k] == sq) ans++;
            }
        }
    }
    return ans;
}

int numTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    return countTriplets(nums1, nums1Size, nums2, nums2Size) +
           countTriplets(nums2, nums2Size, nums1, nums1Size);
}
