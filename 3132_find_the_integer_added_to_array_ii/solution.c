// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

#include <stdlib.h>

static int cmp3132(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

static int check3132(int* a, int n1, int* b, int n2, int x) {
    int i = 0, j = 0, cnt = 0;
    while (i < n1 && j < n2) {
        if (b[j] - a[i] != x) cnt++;
        else j++;
        i++;
    }
    return cnt <= 2;
}

int minimumAddedInteger(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    qsort(nums1, nums1Size, sizeof(int), cmp3132);
    qsort(nums2, nums2Size, sizeof(int), cmp3132);
    int ans = 1 << 30;
    for (int t = 0; t < 3 && t < nums1Size; t++) {
        int x = nums2[0] - nums1[t];
        if (check3132(nums1, nums1Size, nums2, nums2Size, x) && x < ans) ans = x;
    }
    return ans;
}
