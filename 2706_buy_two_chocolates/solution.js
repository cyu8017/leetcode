// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

var buyChoco = function(prices, money) {
    prices = prices.slice().sort((a, b) => a - b);
    const cost = prices[0] + prices[1];
    return cost <= money ? money - cost : money;
};
