// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

var countOfPairs = function(nums) {
    const mod = 1000000007;
    const n = nums.length;
    let dp = new Array(51).fill(0);
    for (let a = 0; a <= nums[0]; a++) dp[a] = 1;
    for (let i = 1; i < n; i++) {
        const ndp = new Array(51).fill(0);
        const pref = new Array(52).fill(0);
        for (let a = 0; a <= 50; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
        for (let a2 = 0; a2 <= nums[i]; a2++) {
            const b2 = nums[i] - a2;
            let maxA1 = a2;
            const lim = nums[i - 1] - b2;
            if (lim < maxA1) maxA1 = lim;
            if (maxA1 < 0) continue;
            if (maxA1 > 50) maxA1 = 50;
            ndp[a2] = pref[maxA1 + 1];
        }
        dp = ndp;
    }
    let ans = 0;
    for (const v of dp) ans = (ans + v) % mod;
    return ans;
};
