// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    return nums.slice().sort((a, b) => (a.length !== b.length ? b.length - a.length : b.localeCompare(a)))[k - 1];
};
