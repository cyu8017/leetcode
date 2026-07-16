"use strict";
// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/
Object.defineProperty(exports, "__esModule", { value: true });
exports.findMedianSortedArrays = findMedianSortedArrays;
function findMedianSortedArrays(nums1, nums2) {
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const m = nums1.length;
    const n = nums2.length;
    const totalLeft = Math.floor((m + n + 1) / 2);
    let lo = 0;
    let hi = m;
    while (lo <= hi) {
        const i = Math.floor((lo + hi) / 2);
        const j = totalLeft - i;
        const nums1LeftMax = i === 0 ? Number.NEGATIVE_INFINITY : nums1[i - 1];
        const nums1RightMin = i === m ? Number.POSITIVE_INFINITY : nums1[i];
        const nums2LeftMax = j === 0 ? Number.NEGATIVE_INFINITY : nums2[j - 1];
        const nums2RightMin = j === n ? Number.POSITIVE_INFINITY : nums2[j];
        if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            if ((m + n) % 2 === 1) {
                return Math.max(nums1LeftMax, nums2LeftMax);
            }
            return (Math.max(nums1LeftMax, nums2LeftMax) + Math.min(nums1RightMin, nums2RightMin)) / 2;
        }
        if (nums1LeftMax > nums2RightMin) {
            hi = i - 1;
        }
        else {
            lo = i + 1;
        }
    }
    return 0;
}
