// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

/**
 * @param {number[]} baseCosts
 * @param {number[]} toppingCosts
 * @param {number} target
 * @return {number}
 */
var closestCost = function(baseCosts, toppingCosts, target) {
    let best = Infinity;

    const dfs = (i, cur) => {
        if (
            Math.abs(cur - target) < Math.abs(best - target) ||
            (Math.abs(cur - target) === Math.abs(best - target) && cur < best)
        ) {
            best = cur;
        }
        if (i === toppingCosts.length || cur >= target) {
            return;
        }
        dfs(i + 1, cur);
        dfs(i + 1, cur + toppingCosts[i]);
        dfs(i + 1, cur + 2 * toppingCosts[i]);
    };

    for (const base of baseCosts) {
        dfs(0, base);
    }
    return best;
};
