// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

function closestCost(baseCosts: number[], toppingCosts: number[], target: number): number {
    let best = Infinity;

    const dfs = (i: number, cur: number): void => {
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
}
