// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
    let lo = 1;
    let hi = Math.max(...nums);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        const sum = nums.reduce((acc, x) => acc + Math.ceil(x / mid), 0);
        if (sum <= threshold) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
