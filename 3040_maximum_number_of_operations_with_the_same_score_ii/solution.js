// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

var maxOperations = function(nums) {
    const n = nums.length;
    let f, s;
    function dfs(i, j) {
        if (j - i < 1) return 0;
        if (f[i][j] !== -1) return f[i][j];
        let ans = 0;
        if (nums[i] + nums[i + 1] === s) ans = Math.max(ans, 1 + dfs(i + 2, j));
        if (nums[i] + nums[j] === s) ans = Math.max(ans, 1 + dfs(i + 1, j - 1));
        if (nums[j - 1] + nums[j] === s) ans = Math.max(ans, 1 + dfs(i, j - 2));
        return f[i][j] = ans;
    }
    function g(i0, j0, score) {
        f = Array.from({length: n}, () => new Array(n).fill(-1));
        s = score;
        return dfs(i0, j0);
    }
    const a = g(2, n - 1, nums[0] + nums[1]);
    const b = g(0, n - 3, nums[n - 1] + nums[n - 2]);
    const c = g(1, n - 2, nums[0] + nums[n - 1]);
    return 1 + Math.max(a, Math.max(b, c));
};
