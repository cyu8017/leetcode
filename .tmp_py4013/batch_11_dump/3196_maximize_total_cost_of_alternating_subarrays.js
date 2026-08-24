// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

var maximumTotalCost = function(nums) {
    const NEG = -1e18;
    const n = nums.length;
    const memo = Array.from({length: n}, () => [NEG, NEG]);
    const dfs = (i, j) => {
        if (i >= n) return 0;
        if (memo[i][j] !== NEG) return memo[i][j];
        let res = nums[i] + dfs(i + 1, 1);
        if (j > 0) res = Math.max(res, -nums[i] + dfs(i + 1, 0));
        return (memo[i][j] = res);
    };
    return dfs(0, 0);
};
