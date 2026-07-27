"use strict";
// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
function maxProfit(inventory, orders) {
    const MOD = 1000000007n;
    inventory = [...inventory].sort((a, b) => b - a);
    inventory.push(0);
    let ans = 0n;
    let remaining = BigInt(orders);
    for (let i = 0; i < inventory.length - 1; i++) {
        const width = BigInt(i + 1);
        const high = BigInt(inventory[i]);
        const low = BigInt(inventory[i + 1]);
        const balls = width * (high - low);
        const take = remaining < balls ? remaining : balls;
        const full = take / width;
        const rem = take % width;
        const bottom = high - full;
        ans += width * (high + bottom + 1n) * full / 2n + rem * bottom;
        remaining -= take;
        if (remaining === 0n)
            break;
    }
    return Number(ans % MOD);
}
