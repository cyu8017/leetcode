// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

var maximumProcessableQueries = function(nums, queries) {
    const n = nums.length;
    const f = Array.from({length: n}, () => new Array(n).fill(0));
    const m = queries.length;
    for (let i = 0; i < n; i++) {
        for (let j = n - 1; j >= i; j--) {
            if (i > 0) {
                const t = f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0;
                f[i][j] = Math.max(f[i][j], f[i - 1][j] + t);
            }
            if (j + 1 < n) {
                const t = f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0;
                f[i][j] = Math.max(f[i][j], f[i][j + 1] + t);
            }
            if (f[i][j] === m) return m;
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const t = f[i][i] < m && nums[i] >= queries[f[i][i]] ? 1 : 0;
        ans = Math.max(ans, f[i][i] + t);
    }
    return ans;
};
