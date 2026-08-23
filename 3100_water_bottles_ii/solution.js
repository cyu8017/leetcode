// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    let ans = numBottles;
    while (numBottles >= numExchange) {
        numBottles -= numExchange;
        numExchange++;
        ans++;
        numBottles++;
    }
    return ans;
};
