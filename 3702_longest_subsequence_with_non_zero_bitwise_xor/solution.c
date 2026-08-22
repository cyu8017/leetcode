// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

int longestSubsequence(int* nums, int numsSize) {
    int xor = 0, cnt0 = 0;
    for (int i = 0; i < numsSize; i++) {
        xor ^= nums[i];
        if (nums[i] == 0) cnt0++;
    }
    if (xor != 0) return numsSize;
    if (cnt0 == numsSize) return 0;
    return numsSize - 1;
}
