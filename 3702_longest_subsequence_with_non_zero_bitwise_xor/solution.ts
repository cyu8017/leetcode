// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

export function longestSubsequence(nums: any): any {
    let xorv = 0, cnt0 = 0;
    for (const x of nums) {
        xorv ^= x;
        if (x === 0) cnt0++;
    }
    const n = nums.length;
    if (xorv !== 0) return n;
    if (cnt0 === n) return 0;
    return n - 1;
}
