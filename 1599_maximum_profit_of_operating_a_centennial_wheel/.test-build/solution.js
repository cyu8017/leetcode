"use strict";
// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
// @ts-nocheck
function minOperationsMaxProfit(customers, boardingCost, runningCost) {
    let waiting = 0, profit = 0, best = 0, answer = 0, rotation = 0, i = 0;
    while (i < customers.length || waiting) {
        if (i < customers.length)
            waiting += customers[i];
        const boarded = Math.min(4, waiting);
        waiting -= boarded;
        rotation++;
        profit += boarded * boardingCost - runningCost;
        if (profit > best) {
            best = profit;
            answer = rotation;
        }
        i++;
    }
    return best > 0 ? answer : -1;
}
