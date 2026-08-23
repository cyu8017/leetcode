// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

var sortByAbsoluteValue = function(nums) {
    nums.sort((a, b) => Math.abs(a) - Math.abs(b));
    return nums;
};
