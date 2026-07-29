"use strict";
// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
function minScoreTriangulation(values) {
    const n = values.length;
    const memo = Array.from({ length: n }, () => new Array(n).fill(-1));
    const dp = (i, j) => {
        if (j - i < 2)
            return 0;
        if (memo[i][j] !== -1)
            return memo[i][j];
        let best = Infinity;
        for (let k = i + 1; k < j; k++) {
            best = Math.min(best, dp(i, k) + values[i] * values[k] * values[j] + dp(k, j));
        }
        memo[i][j] = best;
        return best;
    };
    return dp(0, n - 1);
}
