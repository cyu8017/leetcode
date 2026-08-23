// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if (original.length !== m * n) return [];
    const ans = Array.from({length: m}, () => new Array(n));
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) ans[i][j] = original[i * n + j];
    return ans;
};
