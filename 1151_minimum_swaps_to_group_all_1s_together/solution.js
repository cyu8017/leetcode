// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

/**
 * @param {number[]} data
 * @return {number}
 */
var minSwaps = function(data) {
    const ones = data.reduce((a, b) => a + b, 0);
    if (ones <= 1) return 0;
    let cur = 0;
    for (let i = 0; i < ones; i++) cur += data[i];
    let best = cur;
    for (let i = ones; i < data.length; i++) {
        cur += data[i] - data[i - ones];
        best = Math.max(best, cur);
    }
    return ones - best;
};
