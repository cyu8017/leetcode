// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

/**
 * @param {number[][]} costs
 * @return {number}
 */
var minCostII = function(costs) {
    if (!costs.length) {
        return 0;
    }
    const colorCount = costs[0].length;
    let previous = costs[0].slice();
    for (let row = 1; row < costs.length; row++) {
        const minCost = Math.min(...previous);
        const minIndex = previous.indexOf(minCost);
        const secondMin = Math.min(
            ...previous.filter((_, index) => index !== minIndex),
        );
        const current = [];
        for (let color = 0; color < colorCount; color++) {
            const extra = color === minIndex ? secondMin : minCost;
            current.push(costs[row][color] + extra);
        }
        previous = current;
    }
    return Math.min(...previous);
};
