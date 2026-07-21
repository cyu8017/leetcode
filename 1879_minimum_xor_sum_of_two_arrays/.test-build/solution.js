"use strict";
// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
function minimumXORSum(nums1, nums2) {
    const n = nums1.length;
    const dp = new Array(1 << n).fill(Infinity);
    dp[0] = 0;
    for (let mask = 0; mask < (1 << n); mask++) {
        const i = mask.toString(2).split("1").length - 1;
        if (i >= n)
            continue;
        for (let j = 0; j < n; j++) {
            if (mask & (1 << j))
                continue;
            const next = mask | (1 << j);
            const cost = dp[mask] + (nums1[i] ^ nums2[j]);
            if (cost < dp[next])
                dp[next] = cost;
        }
    }
    return dp[(1 << n) - 1];
}
