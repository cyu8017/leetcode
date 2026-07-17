// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

import java.util.Arrays;

class Solution {
    public int[] largestSubarray(int[] nums, int k) {
        int start = 0;
        for (int i = 1; i + k <= nums.length; i++) {
            if (nums[i] > nums[start]) {
                start = i;
            }
        }
        return Arrays.copyOfRange(nums, start, start + k);
    }
}
