// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

export function reduce(nums: any, fn: any, init: any): any {
    let acc = init;
    for (const x of nums) acc = fn(acc, x);
    return acc;
}
