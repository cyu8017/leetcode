// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countElements = function(nums) {
    let mn = nums[0], mx = nums[0];
    for (const x of nums) { mn = Math.min(mn, x); mx = Math.max(mx, x); }
    let ans = 0;
    for (const x of nums) if (x > mn && x < mx) ans++;
    return ans;
};
