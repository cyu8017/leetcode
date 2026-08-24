// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

export function matrixReshape(mat: number[][], r: number, c: number): number[][] {
    const rows = mat.length, cols = mat[0].length;
    if (rows * cols !== r * c) return mat;
    const result = Array.from({ length: r }, () => Array(c).fill(0));
    let index = 0;
    for (let i = 0; i < r; ++i) {
        for (let j = 0; j < c; ++j) {
            result[i][j] = mat[Math.floor(index / cols)][index % cols];
            ++index;
        }
    }
    return result;
}
