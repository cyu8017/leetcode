// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

export function map(arr: any, fn: any): any {
    const out = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) out[i] = fn(arr[i], i);
    return out;
}
