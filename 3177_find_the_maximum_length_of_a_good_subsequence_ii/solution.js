// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

var maximumLength = function(nums, k) {
    const n = nums.length;
    const f = Array.from({length: n}, () => new Array(k + 1).fill(0));
    const mp = Array.from({length: k + 1}, () => new Map());
    const g = Array.from({length: k + 1}, () => [0, 0, 0]);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let h = 0; h <= k; h++) {
            f[i][h] = mp[h].get(nums[i]) || 0;
            if (h > 0) {
                if (g[h - 1][0] !== nums[i]) f[i][h] = Math.max(f[i][h], g[h - 1][1]);
                else f[i][h] = Math.max(f[i][h], g[h - 1][2]);
            }
            f[i][h]++;
            mp[h].set(nums[i], Math.max(mp[h].get(nums[i]) || 0, f[i][h]));
            if (g[h][0] !== nums[i]) {
                if (f[i][h] >= g[h][1]) {
                    g[h][2] = g[h][1];
                    g[h][1] = f[i][h];
                    g[h][0] = nums[i];
                } else if (f[i][h] > g[h][2]) {
                    g[h][2] = f[i][h];
                }
            } else if (f[i][h] > g[h][1]) {
                g[h][1] = f[i][h];
            }
            ans = Math.max(ans, f[i][h]);
        }
    }
    return ans;
};
