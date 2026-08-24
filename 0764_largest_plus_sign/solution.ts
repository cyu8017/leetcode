// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

export function orderOfLargestPlusSign(n: number, mines: number[][]): number {
    const banned = new Set();
    for (const mine of mines) banned.add(mine[0] * n + mine[1]);
    const arms = Array.from({length: n}, () => new Array(n).fill(0));
    let best = 0;
    for (let r = 0; r < n; r++) {
        let count = 0;
        for (let c = 0; c < n; c++) {
            count = banned.has(r * n + c) ? 0 : count + 1;
            arms[r][c] = count;
        }
        count = 0;
        for (let c = n - 1; c >= 0; c--) {
            count = banned.has(r * n + c) ? 0 : count + 1;
            arms[r][c] = Math.min(arms[r][c], count);
        }
    }
    for (let c = 0; c < n; c++) {
        let count = 0;
        for (let r = 0; r < n; r++) {
            count = banned.has(r * n + c) ? 0 : count + 1;
            arms[r][c] = Math.min(arms[r][c], count);
        }
        count = 0;
        for (let r = n - 1; r >= 0; r--) {
            count = banned.has(r * n + c) ? 0 : count + 1;
            arms[r][c] = Math.min(arms[r][c], count);
            best = Math.max(best, arms[r][c]);
        }
    }
    return best;
}
