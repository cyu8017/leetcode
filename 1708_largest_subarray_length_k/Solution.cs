// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

public class Solution {
    public int[] LargestSubarray(int[] nums, int k) {
        int start = 0;
        for (int i = 1; i + k <= nums.Length; i++) {
            if (nums[i] > nums[start]) {
                start = i;
            }
        }
        int[] result = new int[k];
        Array.Copy(nums, start, result, 0, k);
        return result;
    }
}
