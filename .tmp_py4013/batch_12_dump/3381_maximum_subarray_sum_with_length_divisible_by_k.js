// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

var maxSubarraySum = function(nums, k) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    const INF = Number.MAX_SAFE_INTEGER;
    const best = new Array(k).fill(INF);
    best[0] = 0;
    let ans = -Number.MAX_SAFE_INTEGER;
    for (let i = 1; i <= n; i++) {
        const r = i % k;
        if (best[r] !== INF) {
            const cand = pref[i] - best[r];
            if (cand > ans) ans = cand;
        }
        if (pref[i] < best[r]) best[r] = pref[i];
    }
    return ans;
};
