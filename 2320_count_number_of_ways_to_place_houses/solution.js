// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

/**
 * @param {number} n
 * @return {number}
 */
var countHousePlacements = function(n) {
    const mod = 1000000007;
    let a = 1, b = 1;
    for (let i = 1; i <= n; ++i) {
        const na = (a + b) % mod;
        b = a;
        a = na;
    }
    const ways = (a + b) % mod;
    return Number(BigInt(ways) * BigInt(ways) % BigInt(mod));
};
