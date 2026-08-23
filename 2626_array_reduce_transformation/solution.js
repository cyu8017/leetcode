// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

var reduce = function(nums, fn, init) {
    let acc = init;
    for (const x of nums) acc = fn(acc, x);
    return acc;
};
