// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

export function knightProbability(n: number, k: number, row: number, column: number): number {
    const moves = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]];
    let dp = Array.from({length: n}, () => new Array(n).fill(0.0));
    dp[row][column] = 1.0;
    for (let step = 0; step < k; step++) {
        const nxt = Array.from({length: n}, () => new Array(n).fill(0.0));
        for (let r = 0; r < n; r++) {
            for (let c = 0; c < n; c++) {
                if (dp[r][c] === 0.0) continue;
                for (const move of moves) {
                    const nr = r + move[0], nc = c + move[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n) nxt[nr][nc] += dp[r][c] / 8.0;
                }
            }
        }
        dp = nxt;
    }
    let total = 0.0;
    for (let r = 0; r < n; r++)
        for (let c = 0; c < n; c++)
            total += dp[r][c];
    return total;
}
