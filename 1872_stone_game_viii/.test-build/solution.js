"use strict";
// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/
function stoneGameVIII(stones) {
    const n = stones.length;
    for (let i = 1; i < n; i++)
        stones[i] += stones[i - 1];
    let score = stones[n - 1];
    for (let i = n - 2; i > 0; i--) {
        score = Math.max(stones[i] - score, score);
    }
    return score;
}
