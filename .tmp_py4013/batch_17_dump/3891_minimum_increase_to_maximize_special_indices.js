// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

var minIncrease = function(nums) {
    const n = nums.length;
    const f = Array.from({length: n}, () => [-1, -1]);
    const dfs = (i, j) => {
        if (i >= n - 1) return 0;
        if (f[i][j] !== -1) return f[i][j];
        const cost = Math.max(0, Math.max(nums[i - 1], nums[i + 1]) + 1 - nums[i]);
        let ans = cost + dfs(i + 2, j);
        if (j > 0) ans = Math.min(ans, dfs(i + 1, 0));
        return f[i][j] = ans;
    };
    return dfs(1, (n & 1) ^ 1);
};
