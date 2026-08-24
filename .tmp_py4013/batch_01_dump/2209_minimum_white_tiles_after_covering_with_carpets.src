// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

/**
 * @param {string} floor
 * @param {number} numCarpets
 * @param {number} carpetLen
 * @return {number}
 */
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    const n = floor.length;
    const INF = 1 << 30;
    const dp = Array.from({length: numCarpets + 1}, () => new Array(n + 1).fill(INF));
    dp[0][0] = 0;
    for (let j = 1; j <= n; j++)
        dp[0][j] = dp[0][j - 1] + (floor[j - 1] === '1' ? 1 : 0);
    for (let c = 1; c <= numCarpets; c++) {
        dp[c][0] = 0;
        for (let j = 1; j <= n; j++) {
            dp[c][j] = dp[c][j - 1] + (floor[j - 1] === '1' ? 1 : 0);
            const start = Math.max(0, j - carpetLen);
            dp[c][j] = Math.min(dp[c][j], dp[c - 1][start]);
        }
    }
    return dp[numCarpets][n];
};
