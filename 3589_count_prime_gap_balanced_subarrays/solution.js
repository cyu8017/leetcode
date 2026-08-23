// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

var primeSubarray = function(nums, k) {
    let mx = 0;
    for (const v of nums) mx = Math.max(mx, v);
    const isPrime = new Array(mx + 1).fill(false);
    for (let i = 2; i <= mx; i++) isPrime[i] = true;
    for (let i = 2; i * i <= mx; i++)
        if (isPrime[i])
            for (let j = i * i; j <= mx; j += i) isPrime[j] = false;
    const n = nums.length;
    let ans = 0;
    for (let l = 0; l < n; l++) {
        const primes = [];
        for (let r = l; r < n; r++) {
            if (isPrime[nums[r]]) primes.push(nums[r]);
            if (primes.length >= 2) {
                let mn = primes[0], mxp = primes[0];
                for (const p of primes) {
                    mn = Math.min(mn, p);
                    mxp = Math.max(mxp, p);
                }
                if (mxp - mn <= k) ans++;
            }
        }
    }
    return ans;
};
