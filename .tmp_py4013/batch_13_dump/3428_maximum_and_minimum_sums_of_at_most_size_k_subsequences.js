// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

var minMaxSums = function(nums, k) {
    const mod = 1000000007;
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const C = Array.from({ length: n + 1 }, () => new Array(k).fill(0));
    for (let i = 0; i <= n; i++) {
        C[i][0] = 1;
        for (let j = 1; j < k && j <= i; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let waysMax = 0;
        for (let j = 0; j < k && j <= i; j++) waysMax = (waysMax + C[i][j]) % mod;
        let waysMin = 0;
        const right = n - i - 1;
        for (let j = 0; j < k && j <= right; j++) waysMin = (waysMin + C[right][j]) % mod;
        ans = (ans + nums[i] * waysMax % mod + nums[i] * waysMin % mod) % mod;
    }
    return ans;
};
