// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

int longestSubarray(int* nums, int numsSize) {
    int left = 0, zeros = 0, ans = 0;
    for (int right = 0; right < numsSize; right++) {
        zeros += nums[right] == 0;
        while (zeros > 1) {
            zeros -= nums[left] == 0;
            left++;
        }
        if (right - left > ans) ans = right - left;
    }
    return ans;
}
