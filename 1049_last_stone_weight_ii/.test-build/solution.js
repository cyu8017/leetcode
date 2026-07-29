"use strict";
// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/
function lastStoneWeightII(stones) {
    const total = stones.reduce((a, b) => a + b, 0);
    let reachable = new Set([0]);
    for (const stone of stones) {
        const next = new Set(reachable);
        for (const s of reachable)
            next.add(s + stone);
        reachable = next;
    }
    let best = total;
    for (const s of reachable)
        best = Math.min(best, Math.abs(total - 2 * s));
    return best;
}
