// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var maxSum = function(nums, m, k) {
    const freq = new Map();
    let sum = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        sum += nums[i];
        if (i >= k) {
            const out = nums[i - k];
            sum -= out;
            const c = (freq.get(out) || 0) - 1;
            if (c === 0) freq.delete(out);
            else freq.set(out, c);
        }
        if (i >= k - 1 && freq.size >= m) ans = Math.max(ans, sum);
    }
    return ans;
};
