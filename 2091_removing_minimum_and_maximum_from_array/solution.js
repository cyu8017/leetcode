// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeletions = function(nums) {
    const n = nums.length;
    let mi = 0, ma = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] < nums[mi]) mi = i;
        if (nums[i] > nums[ma]) ma = i;
    }
    if (mi > ma) { const t = mi; mi = ma; ma = t; }
    return Math.min(ma + 1, Math.min(n - mi, mi + 1 + n - ma));
};
