// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

var minCuttingCost = function(n, m, k) {
    const x = Math.max(n, m);
    if (x <= k) return 0;
    return k * (x - k);
};
