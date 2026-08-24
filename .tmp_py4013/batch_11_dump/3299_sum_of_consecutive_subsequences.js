// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

var rangeSum = function(nums) {
    const mod = 1000000007;
    const cnt = new Map();
    const sum = new Map();
    let ans = 0;
    for (const x of nums) {
        const cL = cnt.get(x - 1) || 0, sL = sum.get(x - 1) || 0;
        const cR = cnt.get(x + 1) || 0, sR = sum.get(x + 1) || 0;
        let c = (1 + cL + cR) % mod;
        let s = (x + sL + (cL * x % mod) + sR + (cR * x % mod)) % mod;
        if (cL > 0 && cR > 0) {
            c = (c + (cL * cR % mod)) % mod;
            s = (s + (sL * cR % mod) + (sR * cL % mod) + (cL * cR % mod * x % mod)) % mod;
        }
        cnt.set(x, ((cnt.get(x) || 0) + c) % mod);
        sum.set(x, ((sum.get(x) || 0) + s) % mod);
        ans = (ans + s) % mod;
    }
    return ans;
};
