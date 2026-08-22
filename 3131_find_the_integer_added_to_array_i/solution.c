// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

int addedInteger(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums1Size; (void)nums2Size;
    int mn1 = nums1[0], mn2 = nums2[0];
    for (int i = 1; i < nums1Size; i++) if (nums1[i] < mn1) mn1 = nums1[i];
    for (int i = 1; i < nums2Size; i++) if (nums2[i] < mn2) mn2 = nums2[i];
    return mn2 - mn1;
}
