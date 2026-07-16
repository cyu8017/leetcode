// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

export function calculateMinimumHP(dungeon: number[][]): number {
    const rows = dungeon.length;
    const cols = dungeon[0].length;
    const dp = Array.from({ length: rows + 1 }, () => Array<number>(cols + 1).fill(Infinity));
    dp[rows][cols - 1] = 1;
    dp[rows - 1][cols] = 1;

    for (let row = rows - 1; row >= 0; row -= 1) {
        for (let col = cols - 1; col >= 0; col -= 1) {
            const need = Math.min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col];
            dp[row][col] = Math.max(1, need);
        }
    }
    return dp[0][0];
}