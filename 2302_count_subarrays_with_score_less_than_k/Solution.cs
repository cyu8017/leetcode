// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

public class Solution {
    public long CountSubarrays(int[] nums, long k) {
        long ans = 0, sum = 0;
        int left = 0;
        for (int right = 0; right < nums.Length; right++) {
            sum += nums[right];
            while (sum * (right - left + 1) >= k) {
                sum -= nums[left];
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
