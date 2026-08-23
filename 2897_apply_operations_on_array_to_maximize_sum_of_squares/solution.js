// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSum = function(nums, k) {
    const mod = 1000000007;
    const cnt = Array(32).fill(0);
    for (const v of nums)
        for (let b = 0; b < 32; b++)
            if ((v & (1 << b)) !== 0) cnt[b]++;
    let ans = 0;
    for (let i = 0; i < k; i++) {
        let cur = 0;
        for (let b = 0; b < 32; b++) {
            if (cnt[b] > 0) {
                cur |= 1 << b;
                cnt[b]--;
            }
        }
        ans = (ans + ((cur % mod) * (cur % mod)) % mod) % mod;
    }
    return ans;
};
