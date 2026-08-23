// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

using System.Collections.Generic;

public class Solution {
    public int SubarraysWithKDistinct(int[] nums, int k) {
        int AtMost(int m) {
            if (m < 0) return 0;
            var count = new Dictionary<int, int>();
            int left = 0, ans = 0;
            for (int right = 0; right < nums.Length; right++) {
                if (!count.ContainsKey(nums[right])) count[nums[right]] = 0;
                count[nums[right]]++;
                while (count.Count > m) {
                    if (--count[nums[left]] == 0) count.Remove(nums[left]);
                    left++;
                }
                ans += right - left + 1;
            }
            return ans;
        }
        return AtMost(k) - AtMost(k - 1);
    }
}
