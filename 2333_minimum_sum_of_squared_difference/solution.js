// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k1
 * @param {number} k2
 * @return {number}
 */
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    const n = nums1.length;
    const diff = Array(n);
    let maxD = 0;
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums1[i] - nums2[i]);
        diff[i] = d;
        if (d > maxD) maxD = d;
    }
    let k = k1 + k2;
    const freq = Array(maxD + 1).fill(0);
    for (const d of diff) freq[d]++;
    for (let d = maxD; d > 0 && k > 0; d--) {
        if (freq[d] === 0) continue;
        let take = freq[d];
        if (take > k) take = k;
        freq[d] -= take;
        freq[d - 1] += take;
        k -= take;
    }
    let ans = 0;
    for (let d = 0; d <= maxD; d++) ans += d * d * freq[d];
    return ans;
};
