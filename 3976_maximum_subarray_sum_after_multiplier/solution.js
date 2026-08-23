// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

var maxSubarraySum = function(nums, k) {
    const n = nums.length;
    const inf = Number.MIN_SAFE_INTEGER / 4;
    const f = Array.from({length: n + 1}, () => new Array(4).fill(inf));
    f[0][0] = 0;
    let ans = inf;
    for (let i = 1; i <= n; i++) {
        const x = nums[i - 1];
        f[i][0] = Math.max(f[i - 1][0], 0) + x;
        f[i][1] = Math.max(Math.max(f[i - 1][0], f[i - 1][1]), 0) + x * k;
        f[i][2] = Math.max(Math.max(f[i - 1][0], f[i - 1][2]), 0) + Math.trunc(x / k);
        f[i][3] = Math.max(Math.max(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x;
        ans = Math.max(ans, Math.max(Math.max(f[i][0], f[i][1]), Math.max(f[i][2], f[i][3])));
    }
    return ans;
};
