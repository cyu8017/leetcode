// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    costs = [...costs].sort((a, b) => a - b);
    let count = 0;
    for (const cost of costs) {
        if (coins < cost) break;
        coins -= cost;
        count += 1;
    }
    return count;
};
