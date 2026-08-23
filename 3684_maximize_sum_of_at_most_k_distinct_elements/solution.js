// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

var maxKDistinct = function(nums, k) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const ans = [];
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n && nums[i] === nums[i + 1]) continue;
        ans.push(nums[i]);
        if (--k === 0) break;
    }
    return ans;
};
