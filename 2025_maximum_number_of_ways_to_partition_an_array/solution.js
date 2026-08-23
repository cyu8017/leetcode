// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var waysToPartition = function(nums, k) {
    const n = nums.length;
    const pref = new Array(n);
    pref[0] = nums[0];
    for (let i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
    const total = pref[n - 1];
    const right = new Map(), left = new Map();
    for (let i = 0; i < n - 1; i++) right.set(pref[i], (right.get(pref[i]) || 0) + 1);
    let ans = 0;
    if (total % 2 === 0) ans = right.get(total / 2) || 0;
    for (let i = 0; i < n; i++) {
        const diff = k - nums[i];
        const newTotal = total + diff;
        let cur = 0;
        if (newTotal % 2 === 0) {
            const half = newTotal / 2;
            cur = (left.get(half) || 0) + (right.get(half - diff) || 0);
        }
        ans = Math.max(ans, cur);
        if (i < n - 1) {
            left.set(pref[i], (left.get(pref[i]) || 0) + 1);
            right.set(pref[i], right.get(pref[i]) - 1);
        }
    }
    return ans;
};
