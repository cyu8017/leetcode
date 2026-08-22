// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

int longestSubarray(int* nums, int numsSize) {
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int ans = 0, cur = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == mx) { cur++; if (cur > ans) ans = cur; }
        else cur = 0;
    }
    return ans;
}
