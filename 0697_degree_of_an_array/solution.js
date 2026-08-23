// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    const first = new Map(), last = new Map(), count = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (!first.has(nums[i])) first.set(nums[i], i);
        last.set(nums[i], i);
        count.set(nums[i], (count.get(nums[i]) || 0) + 1);
    }
    let degree = 0;
    for (const freq of count.values()) degree = Math.max(degree, freq);
    let best = Infinity;
    for (const [key, value] of count) {
        if (value === degree) best = Math.min(best, last.get(key) - first.get(key) + 1);
    }
    return best;
};
