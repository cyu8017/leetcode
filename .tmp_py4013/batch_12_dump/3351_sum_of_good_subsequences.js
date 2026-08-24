// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

var sumOfGoodSubsequences = function(nums) {
    const mod = 1000000007;
    const cnt = new Map();
    const sum = new Map();
    let ans = 0;
    for (const x of nums) {
        let c = 1;
        let s = x;
        if ((cnt.get(x - 1) || 0) > 0) {
            c = (c + cnt.get(x - 1)) % mod;
            s = (s + sum.get(x - 1) + cnt.get(x - 1) * x % mod) % mod;
        }
        if ((cnt.get(x + 1) || 0) > 0) {
            c = (c + cnt.get(x + 1)) % mod;
            s = (s + sum.get(x + 1) + cnt.get(x + 1) * x % mod) % mod;
        }
        cnt.set(x, ((cnt.get(x) || 0) + c) % mod);
        sum.set(x, ((sum.get(x) || 0) + s) % mod);
        ans = (ans + s) % mod;
    }
    return ans;
};
