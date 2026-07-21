// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr = [...arr].sort((a, b) => a - b);
    arr[0] = 1;
    for (let i = 1; i < arr.length; i++) arr[i] = Math.min(arr[i], arr[i - 1] + 1);
    return Math.max(...arr);
};
