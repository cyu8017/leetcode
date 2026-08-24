// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

export function new21Game(n: number, k: number, maxPts: number): number {
    if (k === 0 || n >= k - 1 + maxPts) return 1.0;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1.0;
    let window = 1.0, ans = 0.0;
    for (let i = 1; i <= n; i++) {
        dp[i] = window / maxPts;
        if (i < k) window += dp[i];
        else ans += dp[i];
        if (i - maxPts >= 0 && i - maxPts < k) window -= dp[i - maxPts];
    }
    return ans;
}
