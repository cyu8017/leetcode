// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

/**
 * @param {number[]} price
 * @param {number[]} tastiness
 * @param {number} maxAmount
 * @param {number} maxCoupons
 * @return {number}
 */
var maxTastiness = function(price, tastiness, maxAmount, maxCoupons) {
    const n = price.length;
    const NEG = Math.floor(-2147483647 / 2);
    const dp = Array.from({ length: maxAmount + 1 }, () => Array(maxCoupons + 1).fill(NEG));
    dp[0][0] = 0;
    for (let i = 0; i < n; i++) {
        const p = price[i], t = tastiness[i];
        for (let a = maxAmount; a >= 0; a--) {
            for (let c = maxCoupons; c >= 0; c--) {
                if (dp[a][c] < 0) continue;
                if (a + p <= maxAmount) dp[a + p][c] = Math.max(dp[a + p][c], dp[a][c] + t);
                if (c + 1 <= maxCoupons && a + Math.floor(p / 2) <= maxAmount)
                    dp[a + Math.floor(p / 2)][c + 1] = Math.max(dp[a + Math.floor(p / 2)][c + 1], dp[a][c] + t);
            }
        }
    }
    let ans = 0;
    for (let a = 0; a <= maxAmount; a++)
        for (let c = 0; c <= maxCoupons; c++)
            ans = Math.max(ans, dp[a][c]);
    return ans;
};
