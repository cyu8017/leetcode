// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

function oddCells(m: number, n: number, indices: number[][]): number {
    const rows = Array(m).fill(0);
    const cols = Array(n).fill(0);
    for (const [r, c] of indices) {
        rows[r] ^= 1;
        cols[c] ^= 1;
    }
    let answer = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            answer += rows[r] ^ cols[c];
        }
    }
    return answer;
}
