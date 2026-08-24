// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

export function minFlips(grid: any): any {
    const m = grid.length, n = grid[0].length;
    let ans = 0;
    for (let i = 0; i < Math.floor(m / 2); i++) {
        for (let j = 0; j < Math.floor(n / 2); j++) {
            const x = m - i - 1, y = n - j - 1;
            const cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y];
            ans += Math.min(cnt1, 4 - cnt1);
        }
    }
    if (m % 2 === 1 && n % 2 === 1) ans += grid[Math.floor(m / 2)][Math.floor(n / 2)];
    let diff = 0, ones = 0;
    if (m % 2 === 1) {
        for (let j = 0; j < Math.floor(n / 2); j++) {
            if (grid[Math.floor(m / 2)][j] === grid[Math.floor(m / 2)][n - j - 1]) ones += grid[Math.floor(m / 2)][j] * 2;
            else diff += 1;
        }
    }
    if (n % 2 === 1) {
        for (let i = 0; i < Math.floor(m / 2); i++) {
            if (grid[i][Math.floor(n / 2)] === grid[m - i - 1][Math.floor(n / 2)]) ones += grid[i][Math.floor(n / 2)] * 2;
            else diff += 1;
        }
    }
    if (ones % 4 === 0 || diff > 0) ans += diff;
    else ans += 2;
    return ans;
}
