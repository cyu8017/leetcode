// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    let ans = target[0];
    for (let i = 1; i < target.length; i++) {
        ans += Math.max(0, target[i] - target[i - 1]);
    }
    return ans;
};
