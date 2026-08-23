// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

var delayedCount = function(nums, k) {
    const n = nums.length;
    const cnt = new Map();
    const ans = new Array(n).fill(0);
    for (let i = n - k - 2; i >= 0; i--) {
        const key = nums[i + k + 1];
        cnt.set(key, (cnt.get(key) || 0) + 1);
        ans[i] = cnt.get(nums[i]) || 0;
    }
    return ans;
};
