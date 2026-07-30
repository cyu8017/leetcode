// LeetCode 1493 - Longest Subarray Of 1s After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

public class Solution {
    public int LongestSubarray(int[] nums) {
        int left = 0, zeros = 0, ans = 0;
        for (int right = 0; right < nums.Length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > 1) { if (nums[left++] == 0) zeros--; }
            ans = System.Math.Max(ans, right - left);
        }
        return ans;
    }
}
