// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

function findBall(grid: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const ans: number[] = [];
    for (let start = 0; start < n; start++) {
        let col = start;
        for (let row = 0; row < m; row++) {
            const next = col + grid[row][col];
            if (next < 0 || next === n || grid[row][next] !== grid[row][col]) {
                col = -1;
                break;
            }
            col = next;
        }
        ans.push(col);
    }
    return ans;
}
