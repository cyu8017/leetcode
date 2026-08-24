// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

var minXor = function(grid) {
    const rows = grid.length, cols = grid[0].length;
    let dp = Array.from({length: cols}, () => new Array(1024).fill(false));
    for (let row = 0; row < rows; row++) {
        let left = new Array(1024).fill(false);
        for (let col = 0; col < cols; col++) {
            const next = new Array(1024).fill(false);
            const value = grid[row][col];
            if (row === 0 && col === 0) {
                next[value] = true;
            } else {
                for (let xorv = 0; xorv < 1024; xorv++) {
                    if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true;
                }
            }
            dp[col] = next;
            left = next;
        }
    }
    for (let xorv = 0; xorv < 1024; xorv++) {
        if (dp[cols - 1][xorv]) return xorv;
    }
    return -1;
};
