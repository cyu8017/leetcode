// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

export function maxValueOfCoins(piles: number[][], k: number): number {
    let dp = new Array(k + 1).fill(0);
    for (const pile of piles) {
        const ndp = dp.slice();
        let sum = 0;
        for (let take = 1; take <= pile.length && take <= k; take++) {
            sum += pile[take - 1];
            for (let j = take; j <= k; j++)
                ndp[j] = Math.max(ndp[j], dp[j - take] + sum);
        }
        dp = ndp;
    }
    return dp[k];
}
