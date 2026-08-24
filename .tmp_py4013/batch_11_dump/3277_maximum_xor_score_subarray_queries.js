// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

var maximumSubarrayXor = function(nums, queries) {
    const n = nums.length;
    const f = Array.from({length: n}, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) f[i][i] = nums[i];
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i + length - 1 < n; i++) {
            const j = i + length - 1;
            f[i][j] = f[i][j - 1] ^ f[i + 1][j];
        }
    }
    const best = Array.from({length: n}, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) best[i][i] = f[i][i];
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i + length - 1 < n; i++) {
            const j = i + length - 1;
            best[i][j] = Math.max(f[i][j], best[i][j - 1], best[i + 1][j]);
        }
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) ans[i] = best[queries[i][0]][queries[i][1]];
    return ans;
};
