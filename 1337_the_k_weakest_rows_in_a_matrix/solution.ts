// LeetCode 1337 - The K Weakest Rows In A Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

function kWeakestRows(mat: number[][], k: number): number[] {
    return [...mat.keys()].sort((a, b: any): any => mat[a].reduce((s, x: any): any => s + x, 0) - mat[b].reduce((s, x: any): any => s + x, 0) || a - b).slice(0, k);
}
