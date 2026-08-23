// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

using System.Collections.Generic;

public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        int ans = 0, left = 0;
        for (int right = 0; right < nums.Length; right++) {
            freq.TryGetValue(nums[right], out int fr);
            freq[nums[right]] = fr + 1;
            while (freq[nums[right]] > k) {
                freq[nums[left]]--;
                left++;
            }
            if (right - left + 1 > ans) ans = right - left + 1;
        }
        return ans;
    }
}
