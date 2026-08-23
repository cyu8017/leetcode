// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

using System;

public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        int mx = nums[0];
        foreach (int v in nums) if (v > mx) mx = v;
        long ans = 0;
        int cnt = 0, left = 0;
        for (int right = 0; right < nums.Length; right++) {
            if (nums[right] == mx) cnt++;
            while (cnt >= k) {
                if (nums[left] == mx) cnt--;
                left++;
            }
            ans += left;
        }
        return ans;
    }
}
