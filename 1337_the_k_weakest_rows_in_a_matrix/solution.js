// LeetCode 1337 - The K Weakest Rows In A Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
    return [...mat.keys()].sort((a, b) => mat[a].reduce((s, x) => s + x, 0) - mat[b].reduce((s, x) => s + x, 0) || a - b).slice(0, k);
};
