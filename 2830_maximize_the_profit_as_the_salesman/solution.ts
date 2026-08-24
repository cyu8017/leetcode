// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

export function maximizeTheProfit(n: number, offers: number[][]): number {
    const byEnd = Array.from({length: n}, () => []);
    for (const o of offers) byEnd[o[1]].push(o);
    const dp = Array(n + 1).fill(0);
    for (let end = 0; end < n; end++) {
        dp[end + 1] = dp[end];
        for (const o of byEnd[end])
            dp[end + 1] = Math.max(dp[end + 1], dp[o[0]] + o[2]);
    }
    return dp[n];
}
