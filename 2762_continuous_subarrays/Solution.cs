// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

using System.Collections.Generic;

public class Solution {
    public long ContinuousSubarrays(int[] nums) {
        long ans = 0;
        int left = 0;
        var freq = new SortedDictionary<int, int>();
        for (int right = 0; right < nums.Length; right++) {
            if (!freq.ContainsKey(nums[right])) freq[nums[right]] = 0;
            freq[nums[right]]++;
            while (true) {
                int mn = 0, mx = 0;
                foreach (var k in freq.Keys) { mn = k; break; }
                foreach (var k in freq.Keys) mx = k;
                if (mx - mn <= 2) break;
                freq[nums[left]]--;
                if (freq[nums[left]] == 0) freq.Remove(nums[left]);
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
