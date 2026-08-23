// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

var numberOfSubmatrices = function(grid) {
    const m = grid.length, n = grid[0].length;
    const s = Array.from({length: m + 1}, () => Array.from({length: n + 1}, () => [0, 0]));
    let ans = 0;
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0];
            if (grid[i - 1][j - 1] === 'X') s[i][j][0]++;
            s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1];
            if (grid[i - 1][j - 1] === 'Y') s[i][j][1]++;
            if (s[i][j][0] > 0 && s[i][j][0] === s[i][j][1]) ans++;
        }
    }
    return ans;
};
