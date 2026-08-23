// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

using System.Collections.Generic;

public class Solution {
    public long CountGood(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        long pairs = 0, ans = 0;
        int left = 0;
        for (int right = 0; right < nums.Length; right++) {
            pairs += freq.GetValueOrDefault(nums[right], 0);
            freq[nums[right]] = freq.GetValueOrDefault(nums[right], 0) + 1;
            while (pairs >= k) {
                ans += nums.Length - right;
                freq[nums[left]]--;
                pairs -= freq[nums[left]];
                left++;
            }
        }
        return ans;
    }
}
