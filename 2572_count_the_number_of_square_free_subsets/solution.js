// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var squareFreeSubsets = function(nums) {
    const MOD = 1000000007;
    const PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    const maskOf = (x) => {
        let mask = 0;
        for (let i = 0; i < PRIMES.length; ++i) {
            const p = PRIMES[i];
            let cnt = 0;
            while (x % p === 0) {
                x = Math.floor(x / p);
                cnt++;
                if (cnt > 1) return -1;
            }
            if (cnt === 1) mask |= 1 << i;
        }
        return mask;
    };
    const dp = new Array(1 << 10).fill(0);
    dp[0] = 1;
    for (const [x, c] of freq) {
        if (x === 1) continue;
        const m = maskOf(x);
        if (m < 0) continue;
        for (let state = (1 << 10) - 1; state >= 0; --state) {
            if ((state & m) === 0) {
                dp[state | m] = (dp[state | m] + dp[state] * c) % MOD;
            }
        }
    }
    let ans = 0;
    for (const v of dp) ans = (ans + v) % MOD;
    const ones = freq.get(1) || 0;
    let mul = 1;
    for (let i = 0; i < ones; ++i) mul = mul * 2 % MOD;
    ans = ans * mul % MOD;
    ans = (ans - 1 + MOD) % MOD;
    return ans;
};
