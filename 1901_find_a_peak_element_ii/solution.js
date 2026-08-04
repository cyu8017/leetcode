// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findPeakGrid = function(mat) {
    const rows = mat.length, cols = mat[0].length;
    let lo = 0, hi = cols - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        let maxRow = 0;
        for (let r = 1; r < rows; r++) {
            if (mat[r][mid] > mat[maxRow][mid]) maxRow = r;
        }
        const left = mid ? mat[maxRow][mid - 1] : -1;
        const right = mid + 1 < cols ? mat[maxRow][mid + 1] : -1;
        if (mat[maxRow][mid] >= left && mat[maxRow][mid] >= right) return [maxRow, mid];
        if (left > mat[maxRow][mid]) hi = mid - 1;
        else lo = mid + 1;
    }
    return [0, 0];
};
