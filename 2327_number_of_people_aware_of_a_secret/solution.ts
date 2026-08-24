// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

export function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    const mod = 1000000007;
    const dp = Array(n + 1).fill(0);
    dp[1] = 1;
    let share = 0;
    for (let day = 2; day <= n; ++day) {
        if (day - delay >= 1) share = (share + dp[day - delay]) % mod;
        if (day - forget >= 1) share = (share - dp[day - forget] + mod) % mod;
        dp[day] = share;
    }
    let ans = 0;
    for (let day = n - forget + 1; day <= n; ++day)
        if (day >= 1) ans = (ans + dp[day]) % mod;
    return ans;
}
