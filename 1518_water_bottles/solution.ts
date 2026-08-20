// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/
// @ts-nocheck

function numWaterBottles(numBottles: number, numExchange: number): number {
    let total = numBottles;
    while (numBottles >= numExchange) {
        const neu = Math.floor(numBottles / numExchange);
        const rem = numBottles % numExchange;
        total += neu;
        numBottles = neu + rem;
    }
    return total;
}
