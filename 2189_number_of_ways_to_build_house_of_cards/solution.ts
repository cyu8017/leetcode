// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

export function houseOfCards(n: number): number {
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let k = 1; 3 * k - 1 <= n; k++) {
        const cost = 3 * k - 1;
        for (let j = n; j >= cost; j--) dp[j] += dp[j - cost];
    }
    return dp[n];
}
