// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

/**
 Do not return anything, modify nums1 in-place instead.
 */
export function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let i = m - 1;
    let j = n - 1;
    let write = m + n - 1;

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
