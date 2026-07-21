"use strict";
// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
function maxValue(n, index, maxSum) {
    const minSideSum = (value, count) => {
        if (value > count) {
            return Math.floor((value - 1 + value - count) * count / 2);
        }
        return Math.floor(value * (value - 1) / 2) + (count - value + 1);
    };
    let lo = 1, hi = maxSum;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        const total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1);
        if (total <= maxSum)
            lo = mid;
        else
            hi = mid - 1;
    }
    return lo;
}
