// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

function f3555(nums, i, j, inf) {
    let mi = inf, mx = -inf, l = -1, r = -1;
    for (let p = i; p <= j; p++) {
        if (nums[p] < mx) r = p;
        else mx = nums[p];
        const q = j - p + i;
        if (nums[q] > mi) l = q;
        else mi = nums[q];
    }
    if (r === -1) return 0;
    return r - l + 1;
}
var minSubarraySort = function(nums, k) {
    const inf = 1 << 30;
    const n = nums.length;
    const ans = [];
    for (let i = 0; i <= n - k; i++) ans.push(f3555(nums, i, i + k - 1, inf));
    return ans;
};
