// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSumScore = function(nums) {
    let total = 0, pref = 0;
    for (const x of nums) total += x;
    let ans = -Infinity;
    for (const x of nums) {
        pref += x;
        ans = Math.max(ans, Math.max(pref, total - pref + x));
    }
    return ans;
};
