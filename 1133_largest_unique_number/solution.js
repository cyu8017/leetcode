// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var largestUniqueNumber = function(nums) {
    const count = new Map();
    for (const x of nums) count.set(x, (count.get(x) || 0) + 1);
    let ans = -1;
    for (const [value, freq] of count) {
        if (freq === 1) ans = Math.max(ans, value);
    }
    return ans;
};
