// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

var longestSubarray = function(nums) {
    const n = nums.length;
    const left = new Array(n).fill(1);
    const right = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
    }
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
    }
    let ans = 0;
    for (const v of left) ans = Math.max(ans, v);
    for (let i = 0; i < n; i++) {
        const a = i > 0 ? left[i - 1] : 0;
        const b = i + 1 < n ? right[i + 1] : 0;
        if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
            ans = Math.max(ans, Math.max(a + 1, b + 1));
        } else {
            ans = Math.max(ans, a + b + 1);
        }
    }
    return ans;
};
