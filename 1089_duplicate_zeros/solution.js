// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    let zeros = 0;
    for (const x of arr) if (x === 0) zeros++;
    const n = arr.length;
    for (let i = n - 1; i >= 0; i--) {
        if (i + zeros < n) arr[i + zeros] = arr[i];
        if (arr[i] === 0) {
            zeros--;
            if (i + zeros < n) arr[i + zeros] = 0;
        }
    }
};
