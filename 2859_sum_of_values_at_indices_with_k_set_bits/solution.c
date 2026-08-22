// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

int sumIndicesWithKSetBits(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int bits = 0, x = i;
        while (x > 0) { bits += x & 1; x >>= 1; }
        if (bits == k) ans += nums[i];
    }
    return ans;
}
