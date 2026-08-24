// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

export function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {
    const MOD = 1000000007;
    let dp = Array.from({ length: m }, () => Array(n).fill(0));
    dp[startRow][startColumn] = 1;
    let result = 0;
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    for (let move = 0; move < maxMove; ++move) {
        const nxt = Array.from({ length: m }, () => Array(n).fill(0));
        for (let row = 0; row < m; ++row) {
            for (let col = 0; col < n; ++col) {
                const ways = dp[row][col];
                if (ways === 0) continue;
                for (const [dr, dc] of dirs) {
                    const nr = row + dr, nc = col + dc;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD;
                    } else {
                        result = (result + ways) % MOD;
                    }
                }
            }
        }
        dp = nxt;
    }
    return result;
}
