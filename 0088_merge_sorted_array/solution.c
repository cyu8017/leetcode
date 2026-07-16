// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    (void)nums1Size;
    (void)nums2Size;
    int i = m - 1;
    int j = n - 1;
    int write = m + n - 1;

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[write] = nums1[i];
            i--;
        } else {
            nums1[write] = nums2[j];
            j--;
        }
        write--;
    }
}
