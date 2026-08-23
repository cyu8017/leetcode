// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

/**
 * @param {number[][]} costs
 * @return {number}
 */
var minCost = function(costs) {
    if (costs.length === 0) {
        return 0;
    }
    let previous = costs[0].slice();
    for (let row = 1; row < costs.length; row++) {
        previous = [
            costs[row][0] + Math.min(previous[1], previous[2]),
            costs[row][1] + Math.min(previous[0], previous[2]),
            costs[row][2] + Math.min(previous[0], previous[1]),
        ];
    }
    return Math.min(previous[0], previous[1], previous[2]);
};
