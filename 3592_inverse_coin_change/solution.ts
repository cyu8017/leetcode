// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

export function findCoins(numWays: any): any {
    const n = numWays.length;
    const dp = new Array(n + 1).fill(0);
    const coins = [];
    dp[0] = 1;
    for (let amt = 1; amt <= n; amt++) {
        const ways = numWays[amt - 1];
        if (dp[amt] === ways) continue;
        if (dp[amt] + 1 === ways) {
            coins.push(amt);
            for (let x = amt; x <= n; x++) dp[x] += dp[x - amt];
            if (dp[amt] !== ways) return [];
            continue;
        }
        return [];
    }
    return coins;
}
