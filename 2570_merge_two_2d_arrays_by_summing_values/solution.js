// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
    const ans = [];
    let i = 0, j = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i][0] === nums2[j][0]) {
            ans.push([nums1[i][0], nums1[i][1] + nums2[j][1]]);
            i++; j++;
        } else if (nums1[i][0] < nums2[j][0]) {
            ans.push([nums1[i][0], nums1[i][1]]);
            i++;
        } else {
            ans.push([nums2[j][0], nums2[j][1]]);
            j++;
        }
    }
    while (i < nums1.length) {
        ans.push([nums1[i][0], nums1[i][1]]);
        i++;
    }
    while (j < nums2.length) {
        ans.push([nums2[j][0], nums2[j][1]]);
        j++;
    }
    return ans;
};
