// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

var splitArray = function(nums) {
    const n = nums.length;
    const s = new Array(n);
    const f = new Array(n).fill(true);
    const g = new Array(n).fill(true);
    s[0] = nums[0];
    for (let i = 1; i < n; i++) {
        s[i] = s[i - 1] + nums[i];
        f[i] = f[i - 1];
        if (nums[i] <= nums[i - 1]) f[i] = false;
    }
    for (let i = n - 2; i >= 0; i--) {
        g[i] = g[i + 1];
        if (nums[i] <= nums[i + 1]) g[i] = false;
    }
    const inf = Number.MAX_SAFE_INTEGER / 4;
    let ans = inf;
    for (let i = 0; i < n - 1; i++) {
        if (f[i] && g[i + 1]) {
            const s1 = s[i], s2 = s[n - 1] - s[i];
            ans = Math.min(ans, Math.abs(s1 - s2));
        }
    }
    return ans < inf ? ans : -1;
};
