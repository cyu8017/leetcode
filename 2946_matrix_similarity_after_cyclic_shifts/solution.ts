// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

export function areSimilar(mat: any, k: any): any {
    const m = mat.length, n = mat[0].length;
    for (let i = 0; i < m; i++) {
        let shift;
        if (i % 2 === 0) {
            shift = n - (k % n);
            if (shift === n) shift = 0;
        } else {
            shift = k % n;
        }
        for (let j = 0; j < n; j++)
            if (mat[i][j] !== mat[i][(j + shift) % n]) return false;
    }
    return true;
}
