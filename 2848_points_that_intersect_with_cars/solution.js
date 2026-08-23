// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

/**
 * @param {number[][]} nums
 * @return {number}
 */
var numberOfPoints = function(nums) {
    const cov = Array(102).fill(0);
    for (const [a, b] of nums)
        for (let x = a; x <= b; x++) cov[x] = 1;
    return cov.reduce((s, v) => s + v, 0);
};
