"use strict";
// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/
function maxJumps(arr, d) {
    const dp = Array(arr.length).fill(1);
    const order = arr.map((value, i) => [value, i]).sort((a, b) => a[0] - b[0]);
    for (const [, i] of order) {
        for (const step of [-1, 1]) {
            let j = i + step;
            while (j >= 0 && j < arr.length && Math.abs(j - i) <= d && arr[j] < arr[i]) {
                dp[i] = Math.max(dp[i], 1 + dp[j]);
                j += step;
            }
        }
    }
    return Math.max(...dp);
}
