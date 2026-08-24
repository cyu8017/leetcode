// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

export function rangeAddQueries(n: number, queries: number[][]): number[][] {
    const diff = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (const q of queries) {
        const r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
        diff[r1][c1]++;
        diff[r1][c2 + 1]--;
        diff[r2 + 1][c1]--;
        diff[r2 + 1][c2 + 1]++;
    }
    const mat = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let v = diff[i][j];
            if (i > 0) v += mat[i - 1][j];
            if (j > 0) v += mat[i][j - 1];
            if (i > 0 && j > 0) v -= mat[i - 1][j - 1];
            mat[i][j] = v;
        }
    }
    return mat;
}
