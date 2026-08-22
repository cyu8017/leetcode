// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

int longestNiceSubarray(int* nums, int numsSize) {
    int used = 0, left = 0, ans = 0;
    for (int right = 0; right < numsSize; right++) {
        while (used & nums[right]) { used ^= nums[left]; left++; }
        used |= nums[right];
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    return ans;
}
