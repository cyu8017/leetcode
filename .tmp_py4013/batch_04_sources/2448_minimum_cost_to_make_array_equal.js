// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

/**
 * @param {number[]} nums
 * @param {number[]} cost
 * @return {number}
 */
var minCost = function(nums, cost) {
    const n = nums.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => nums[a] - nums[b]);
    let totalCost = 0;
    for (const c of cost) totalCost += c;
    let pref = 0, median = 0;
    for (const i of idx) {
        pref += cost[i];
        if (pref * 2 >= totalCost) {
            median = nums[i];
            break;
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let diff = nums[i] - median;
        if (diff < 0) diff = -diff;
        ans += diff * cost[i];
    }
    return ans;
};
