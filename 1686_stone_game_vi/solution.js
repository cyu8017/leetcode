// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

/**
 * @param {number[]} aliceValues
 * @param {number[]} bobValues
 * @return {number}
 */
var stoneGameVI = function(aliceValues, bobValues) {
    const order = [...Array(aliceValues.length).keys()].sort(
        (i, j) => (aliceValues[j] + bobValues[j]) - (aliceValues[i] + bobValues[i])
    );
    let score = 0;
    order.forEach((i, t) => {
        score += t % 2 === 0 ? aliceValues[i] : -bobValues[i];
    });
    return score > 0 ? 1 : score < 0 ? -1 : 0;
};
