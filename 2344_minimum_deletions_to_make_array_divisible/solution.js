// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

/**
 * @param {number[]} nums
 * @param {number[]} numsDivide
 * @return {number}
 */
var minOperations = function(nums, numsDivide) {
    const gcd = (a, b) => {
        while (b !== 0) { const t = a % b; a = b; b = t; }
        return a;
    };
    let g = numsDivide[0];
    for (let i = 1; i < numsDivide.length; i++) g = gcd(g, numsDivide[i]);
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i++) {
        if (g % nums[i] === 0) return i;
    }
    return -1;
};
