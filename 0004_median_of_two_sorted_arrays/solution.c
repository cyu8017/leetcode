// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

#include <limits.h>

static int max_int(int a, int b) {
    return a > b ? a : b;
}

static int min_int(int a, int b) {
    return a < b ? a : b;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    if (nums1Size > nums2Size) {
        int* tmp = nums1;
        nums1 = nums2;
        nums2 = tmp;
        int tmpSize = nums1Size;
        nums1Size = nums2Size;
        nums2Size = tmpSize;
    }

    int m = nums1Size;
    int n = nums2Size;
    int totalLeft = (m + n + 1) / 2;
    int lo = 0;
    int hi = m;

    while (lo <= hi) {
        int i = (lo + hi) / 2;
        int j = totalLeft - i;

        int nums1LeftMax = i == 0 ? INT_MIN : nums1[i - 1];
        int nums1RightMin = i == m ? INT_MAX : nums1[i];
        int nums2LeftMax = j == 0 ? INT_MIN : nums2[j - 1];
        int nums2RightMin = j == n ? INT_MAX : nums2[j];

        if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            if ((m + n) % 2 == 1) {
                return (double)max_int(nums1LeftMax, nums2LeftMax);
            }
            return (max_int(nums1LeftMax, nums2LeftMax) + min_int(nums1RightMin, nums2RightMin)) / 2.0;
        }

        if (nums1LeftMax > nums2RightMin) {
            hi = i - 1;
        } else {
            lo = i + 1;
        }
    }

    return 0.0;
}
