"use strict";
// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
function getMaximumConsecutive(coins) {
    coins.sort((a, b) => a - b);
    let reach = 0;
    for (const coin of coins) {
        if (coin > reach + 1)
            break;
        reach += coin;
    }
    return reach + 1;
}
