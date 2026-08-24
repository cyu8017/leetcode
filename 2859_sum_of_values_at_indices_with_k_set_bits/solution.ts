// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

export function sumIndicesWithKSetBits(nums: number[], k: number): number {
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        let x = i, bits = 0;
        while (x) { bits += x & 1; x >>= 1; }
        if (bits === k) ans += nums[i];
    }
    return ans;
}
