// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    const m = mat.length;
    const n = mat[0].length;
    const prefix = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
        }
    }
    const possible = (size) => {
        for (let r = size; r <= m; r++) {
            for (let c = size; c <= n; c++) {
                const sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
                if (sum <= threshold) return true;
            }
        }
        return false;
    };
    let lo = 0;
    let hi = Math.min(m, n);
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (possible(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
