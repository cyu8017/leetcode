// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var isPossibleDivide = function(nums, k) {
    if (nums.length % k !== 0) return false;
    const counts = new Map();
    for (const x of nums) {
        counts.set(x, (counts.get(x) || 0) + 1);
    }
    const starts = [...counts.keys()].sort((a, b) => a - b);
    for (const start of starts) {
        const amount = counts.get(start) || 0;
        if (!amount) continue;
        for (let value = start; value < start + k; value++) {
            const have = counts.get(value) || 0;
            if (have < amount) return false;
            counts.set(value, have - amount);
        }
    }
    return true;
};
