// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
    const seen = new Map();
    let left = 0, cur = 0, best = 0;
    for (let right = 0; right < nums.length; right++) {
        const x = nums[right];
        if (seen.has(x) && seen.get(x) >= left) {
            const stop = seen.get(x);
            while (left <= stop) cur -= nums[left++];
        }
        seen.set(x, right);
        cur += x;
        best = Math.max(best, cur);
    }
    return best;
};
