"use strict";
// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
// @ts-nocheck
function minCost(n, cuts) {
    const points = [0, ...cuts.slice().sort((a, b) => a - b), n];
    const size = points.length;
    const dp = Array.from({ length: size }, () => Array(size).fill(0));
    for (let width = 2; width < size; width++) {
        for (let left = 0; left + width < size; left++) {
            const right = left + width;
            let best = Infinity;
            for (let mid = left + 1; mid < right; mid++) {
                best = Math.min(best, dp[left][mid] + dp[mid][right]);
            }
            if (best === Infinity)
                best = 0;
            if (right > left + 1)
                best += points[right] - points[left];
            dp[left][right] = best;
        }
    }
    return dp[0][size - 1];
}
