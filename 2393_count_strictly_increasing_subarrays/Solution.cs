// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

public class Solution {
    public long CountSubarrays(int[] nums) {
        long ans = 0, len = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (i > 0 && nums[i] > nums[i - 1]) len++;
            else len = 1;
            ans += len;
        }
        return ans;
    }
}
