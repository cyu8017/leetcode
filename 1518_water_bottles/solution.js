// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let total = numBottles;
    while (numBottles >= numExchange) {
        const neu = Math.floor(numBottles / numExchange);
        const rem = numBottles % numExchange;
        total += neu;
        numBottles = neu + rem;
    }
    return total;
};
