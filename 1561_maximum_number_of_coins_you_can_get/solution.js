// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort((a, b) => a - b);
    let ans = 0;
    for (let i = Math.floor(piles.length / 3); i < piles.length; i += 2) ans += piles[i];
    return ans;
};
