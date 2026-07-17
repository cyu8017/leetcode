"use strict";
// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/
function maxSumAfterOperation(nums) {
    let noSquare = 0;
    let oneSquare = 0;
    let best = -Infinity;
    for (const value of nums) {
        oneSquare = Math.max(oneSquare + value, noSquare + value * value, value * value);
        noSquare = Math.max(noSquare + value, value);
        best = Math.max(best, oneSquare);
    }
    return best;
}
