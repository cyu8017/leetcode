"use strict";
// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/
function canDistribute(nums, quantity) {
    const freq = new Map();
    for (const x of nums)
        freq.set(x, (freq.get(x) || 0) + 1);
    const cnt = [...freq.values()];
    quantity.sort((a, b) => b - a);
    const m = quantity.length;
    const sums = Array(1 << m).fill(0);
    for (let mask = 1; mask < (1 << m); mask++) {
        const bit = mask & -mask;
        sums[mask] = sums[mask ^ bit] + quantity[31 - Math.clz32(bit)];
    }
    let dp = new Set([0]);
    for (const c of cnt) {
        const nxt = new Set(dp);
        for (const mask of dp) {
            let left = ((1 << m) - 1) ^ mask;
            let sub = left;
            while (sub) {
                if (sums[sub] <= c)
                    nxt.add(mask | sub);
                sub = (sub - 1) & left;
            }
        }
        dp = nxt;
    }
    return dp.has((1 << m) - 1);
}
