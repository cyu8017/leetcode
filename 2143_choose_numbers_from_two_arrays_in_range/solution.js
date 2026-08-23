// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var countSubranges = function(nums1, nums2) {
    const MOD = 1000000007;
    const n = nums1.length;
    let ans = 0;
    let dp = new Map();
    for (let i = 0; i < n; i++) {
        const ndp = new Map();
        ndp.set(nums1[i], ((ndp.get(nums1[i]) || 0) + 1) % MOD);
        ndp.set(-nums2[i], ((ndp.get(-nums2[i]) || 0) + 1) % MOD);
        for (const [diff, cnt] of dp) {
            ndp.set(diff + nums1[i], ((ndp.get(diff + nums1[i]) || 0) + cnt) % MOD);
            ndp.set(diff - nums2[i], ((ndp.get(diff - nums2[i]) || 0) + cnt) % MOD);
        }
        dp = ndp;
        ans = (ans + (dp.get(0) || 0)) % MOD;
    }
    return ans;
};
