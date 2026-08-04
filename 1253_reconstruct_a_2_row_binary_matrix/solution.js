// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

/**
 * @param {number} upper
 * @param {number} lower
 * @param {number[]} colsum
 * @return {number[][]}
 */
var reconstructMatrix = function(upper, lower, colsum) {
    const top = Array(colsum.length).fill(0);
    const bottom = Array(colsum.length).fill(0);
    for (let i = 0; i < colsum.length; i++) {
        if (colsum[i] === 2) {
            top[i] = bottom[i] = 1;
            upper--;
            lower--;
        }
    }
    if (upper < 0 || lower < 0) return [];
    for (let i = 0; i < colsum.length; i++) {
        if (colsum[i] === 1) {
            if (upper) {
                top[i] = 1;
                upper--;
            } else if (lower) {
                bottom[i] = 1;
                lower--;
            } else {
                return [];
            }
        }
    }
    return upper === 0 && lower === 0 ? [top, bottom] : [];
};
