// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function(nums, k, edges) {
    let f0 = 0, f1 = -Number.MAX_SAFE_INTEGER;
    for (const x of nums) {
        const nf0 = Math.max(f0 + x, f1 + (x ^ k));
        const nf1 = Math.max(f1 + x, f0 + (x ^ k));
        f0 = nf0;
        f1 = nf1;
    }
    return f0;
};
